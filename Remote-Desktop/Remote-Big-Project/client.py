# Credits are not required but will be nice.
import socket
import tkinter as tk
from tkinter import messagebox
import pickle
import threading
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

class RemoteDesktopClient(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Remote Desktop - Connect")
        self.geometry("400x200")
        self.configure(bg="#1F1F1F")

        self.label = tk.Label(self, text="Enter IP Address:", font=("Helvetica", 14), fg="#FFFFFF", bg="#1F1F1F")
        self.label.pack(pady=20)

        self.ip_entry = tk.Entry(self, font=("Helvetica", 14), width=20)
        self.ip_entry.pack(pady=10)

        self.port_label = tk.Label(self, text="Enter Port:", font=("Helvetica", 14), fg="#FFFFFF", bg="#1F1F1F")
        self.port_label.pack(pady=10)

        self.port_entry = tk.Entry(self, font=("Helvetica", 14), width=20)
        self.port_entry.pack(pady=10)

        self.connect_button = tk.Button(self, text="Connect", font=("Helvetica", 14), command=self.connect)
        self.connect_button.pack(pady=20)

    def connect(self):
        ip_address = self.ip_entry.get()
        port = self.port_entry.get()
        if not ip_address or not port:
            messagebox.showerror("Error", "IP address and port cannot be empty!")
            return

        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((ip_address, int(port)))
        except Exception as e:
            messagebox.showerror("Connection Failed", f"Could not connect to {ip_address} on port {port}: {e}")
            return

        auth_response = self.client_socket.recv(1024)
        if auth_response == b'AUTH_OK':
            messagebox.showinfo("Authorized", "Connection authorized!")
            self.start_session()
        else:
            messagebox.showerror("Authorization Failed", "Connection denied by the host.")

    def start_session(self):
        threading.Thread(target=self.send_mouse_events, daemon=True).start()
        threading.Thread(target=self.send_keyboard_events, daemon=True).start()

    def send_mouse_events(self):
        def on_move(x, y):
            data = {'type': 'mouse_move', 'x': x, 'y': y}
            self.client_socket.send(pickle.dumps(data))

        def on_click(x, y, button, pressed):
            if pressed:
                data = {'type': 'mouse_click', 'x': x, 'y': y}
                self.client_socket.send(pickle.dumps(data))

        with MouseListener(on_move=on_move, on_click=on_click) as listener:
            listener.join()

    def send_keyboard_events(self):
        def on_press(key):
            try:
                data = {'type': 'key_press', 'key': key.char}
            except AttributeError:
                data = {'type': 'key_press', 'key': str(key)}
            self.client_socket.send(pickle.dumps(data))

        with KeyboardListener(on_press=on_press) as listener:
            listener.join()

if __name__ == "__main__":
    app = RemoteDesktopClient()
    app.mainloop()

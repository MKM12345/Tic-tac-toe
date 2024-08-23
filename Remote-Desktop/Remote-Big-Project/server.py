# Credits to MKM12345 will be nice but not required.
import socket
import threading
import tkinter as tk
from tkinter import messagebox
import pyautogui
import pickle

class RemoteDesktopServer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Remote Desktop - Waiting")
        self.geometry("400x200")
        self.configure(bg="#1F1F1F")

        self.label = tk.Label(self, text="Waiting for connection...", font=("Helvetica", 14), fg="#FFFFFF", bg="#1F1F1F")
        self.label.pack(pady=20)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 0))  # Bind to an available port
        self.port = self.server_socket.getsockname()[1]
        self.server_socket.listen(1)

        self.label.config(text=f"Listening on port {self.port}")

        self.client_socket = None

        threading.Thread(target=self.wait_for_connection, daemon=True).start()

    def wait_for_connection(self):
        self.client_socket, addr = self.server_socket.accept()
        self.label.config(text=f"Connection request from {addr[0]}")

        self.ask_authorization(addr[0])

    def ask_authorization(self, ip):
        response = messagebox.askyesno("Connection Request", f"IP {ip} is requesting to connect. Authorize?")
        if response:
            self.client_socket.send(b"AUTH_OK")
            threading.Thread(target=self.start_session, daemon=True).start()
        else:
            self.client_socket.send(b"AUTH_DENIED")
            self.client_socket.close()

    def start_session(self):
        while True:
            try:
                data = self.client_socket.recv(4096)
                if not data:
                    break
                command = pickle.loads(data)
                if command['type'] == 'mouse_move':
                    pyautogui.moveTo(command['x'], command['y'])
                elif command['type'] == 'mouse_click':
                    pyautogui.click(command['x'], command['y'])
                elif command['type'] == 'key_press':
                    pyautogui.press(command['key'])
            except Exception as e:
                print(f"Connection lost: {e}")
                break

        self.client_socket.close()

if __name__ == "__main__":
    app = RemoteDesktopServer()
    app.mainloop()

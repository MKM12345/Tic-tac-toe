import subprocess

def remote_desktop(ip_address):
    try:
        # Launch the RDP client (mstsc) with the given IP address
        subprocess.run(["mstsc", f"/v:{ip_address}"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to {ip_address}. Error: {e}")

if __name__ == "__main__":
    # Prompt the user to input the IP address
    ip_address = input("Enter the IP address of the remote computer: ")


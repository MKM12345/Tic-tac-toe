# Remote Desktop Application

Alright. There are two versions to this. 

If you want to see the short one of the remote desktop apps, go to [short.py](https://github.com/MKM12345/Youtube-Source-Codes/blob/main/Remote-Desktop/short.py).

Otherwise, if you want to see the more established, larger app, that I will include in a future youtube video, follow these instructions below to run it and this [link](https://github.com/MKM12345/Youtube-Source-Codes/blob/main/Remote-Desktop/Remote-Big-Project) to get the program.

Right, thats the side note. Here are the instructions:

## Instructions

This project provides a simple remote desktop solution using Python. It allows one user to control another user's desktop over a network.

## Features
- **Dynamic Port Selection**: Server chooses an available port automatically.
- **Connection Authorization**: Server requests authorization before allowing access.
- **Remote Control**: Client can control the server’s mouse and keyboard.

## Installation

Ensure Python is installed, then install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the server**:

On the machine to be controlled, run:
    ```bash
    python server.py
    ```
Note the displayed port number.

3. **Run the client**:

On the controlling machine, run:

    ```bash
    python client.py
    ```

Enter the server’s IP and port, then connect.

## Notes
- Ensure both machines are on the same network.

  Hope you enjoy the app! Feel free to modify and share :)

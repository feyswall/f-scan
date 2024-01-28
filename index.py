import socket
import pygetwindow as gw
import pyautogui
import time

def input_text_in_active_window(text):
    # Get the active window
    active_window = gw.getActiveWindow()

    if active_window:
        # Activate the window
        active_window.activate()
        # Type the text using pyautogui
        pyautogui.typewrite(text)
        time.sleep(1)  # You might need to adjust this delay based on the application's responsiveness
    else:
        print("No active window found.")

# Set the host and port you want to listen on
host = '192.168.28.252'  # Use '0.0.0.0' to listen on all available interfaces
port = 58627

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections (maximum number of queued connections is 5)
server_socket.listen(5)
print(f"Listening for connections on {host}:{port}")

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()

    print(f"Accepted connection from {client_address}")

    # Receive and print data from the client
    data = client_socket.recv(1024)
    data = str(data)
    print(f"Received Code: {data[2:-1]}")

    # Example: Input text into the active window
    input_text_in_active_window(data[2:-1])

    # Optionally, you can send a response back to the client
    # response = "Hello from the server!"
    # client_socket.send(response)

    # Close the connection with the client
    client_socket.close()
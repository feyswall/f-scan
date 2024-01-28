import socket
from windows.FrontWindows import FrontWindows
from database.QueryBuilder import QueryBuilder

queryBuilder = QueryBuilder()
setups = queryBuilder.get_all_setups()
if(setups != None):
    print("not null")
else:
    print("as Null as Day")

# Set the host and port you want to listen on
host = '0.0.0.0'
port = 58627

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections (maximum number of queued connections is 5)
server_socket.listen(5)
print(f"Listening for connections on {host}:{port}")

while True:
    print("while loop")
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()

    print(f"Accepted connection from {client_address}")

    # Receive and print data from the client
    data = client_socket.recv(1024)

    # removing the surrounding b' '
    data = (str(data))[2:-1]

    # making sure that it comes through our destination source
    if(data[:5] == "zebra"):
        data = data[6:]
        print(f"Received Code: {data}")

        # Example: Input text into the active window
        fw = FrontWindows()
        fw.input_text_in_active_window(data)

        # Optionally, you can send a response back to the client
        # response = "Hello from the server!"
        # client_socket.send(response)

        # Close the connection with the client
        client_socket.close()
    else:
        print(f"Received Code: {data} but it\'s not from our source")

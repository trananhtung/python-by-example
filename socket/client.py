"""
This is the client side of the chat application.
It connects to the server
"""

import socket
import threading

from config import HOST, SERVER_PORT


def receive_messages(client_socket_rev):
    """Function to receive and display messages from the server"""
    while True:
        try:
            rev_message = client_socket_rev.recv(1024).decode("utf-8")
            print(rev_message)
        except:
            # Handle any errors that occur during message reception
            print("Disconnected from the server.")
            break


# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at localhost and port 12345
client_socket.connect((HOST, SERVER_PORT))


receive_thread = threading.Thread(
    target=receive_messages, args=(client_socket,)
)
receive_thread.start()

# Send messages to the server
while True:
    try:
        message = input()
        if message.lower() == "exit":
            # Type 'exit' to disconnect from the server
            client_socket.close()
            break
        client_socket.send(message.encode("utf-8"))
    except:
        client_socket.close()

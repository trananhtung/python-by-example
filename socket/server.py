"""
Server program to handle multiple clients using threads
"""

import socket
import threading

from config import HOST, SERVER_PORT

# List to store all connected client sockets
clients = []


def broadcast_message(message, sender_client):
    """Function to broadcast a message to all connected clients"""
    print(f"Broadcasting message: {message.decode('utf-8')}")
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                # Remove the client from the list if unable to send the message
                clients.remove(client)


def handle_client(sender_client):
    """Function to handle each client's connection"""
    while True:
        try:
            # Receive data from the client
            message = sender_client.recv(1024)
            if not message:
                # Remove the client from the list if no data received
                clients.remove(sender_client)
                break
            # Broadcast the received message to all clients
            broadcast_message(message, sender_client)
        except:
            # Remove the client from the list if an error occurs
            clients.remove(sender_client)
            break


# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to host and port
server_socket.bind((HOST, SERVER_PORT))
server_socket.listen(5)  # Allow up to 5 clients to queue

print("Server is listening for incoming connections...")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Add the client socket to the list of clients
    clients.append(client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket,)
    )
    client_thread.start()

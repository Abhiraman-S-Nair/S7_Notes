import socket
import threading
import subprocess
import time  # Import time for delay

# Prompt the user for the number of clients to create
num_clients = int(input("Enter the number of clients to create: "))

# Global lists to manage clients and their usernames
clients = []
usernames = []

# Broadcast message to all clients
def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message.encode('utf-8'))

# Handle individual client connection
def handle_client(client):
    while True:
        try:
            # Receive message from client
            message = client.recv(1024).decode('utf-8')
            if message == "EXIT":
                # Handle user exiting
                index = clients.index(client)
                username = usernames[index]
                broadcast(f"{username} has left the chat.", client)
                print(f"{username} has disconnected.")
                usernames.remove(username)
                clients.remove(client)
                client.close()
                break
            else:
                # Broadcast the message to all clients
                username = usernames[clients.index(client)]
                broadcast(f"{username}: {message}", client)
                print(f"{username}: {message}")
        except:
            break

# Accept new client connections
def receive_connections():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Request and store username
        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        # Notify all users about the new connection
        print(f"{username} joined the chat.")
        broadcast(f"{username} has joined the chat!", client)
        client.send("Connected to the chat.".encode('utf-8'))

        # Start a new thread to handle client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Initialize server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()

print("Server is listening...")

# Start a thread to accept incoming connections
thread = threading.Thread(target=receive_connections)
thread.start()

# Delay to ensure server setup is complete
time.sleep(2)

# Launch the specified number of clients as subprocesses
for i in range(num_clients):
    subprocess.Popen(['python', 'auto_connect_client.py'])  # Replace with the client script filename

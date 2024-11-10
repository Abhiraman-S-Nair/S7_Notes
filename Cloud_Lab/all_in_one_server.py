import socket
import threading
import string
import subprocess
import time

# List to track connected clients
clients = []

# Text analysis function
def analyze_text(data, specific_word):
    word_count = len(data.split())
    specific_word_count = data.lower().count(specific_word.lower()) if specific_word != "NONE" else 0
    number_count = sum(c.isdigit() for c in data)
    special_char_count = sum(c in string.punctuation for c in data)
    vowel_count = sum(c in 'aeiouAEIOU' for c in data)
    consonant_count = sum(c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' for c in data)

    result = (f"Word Count: {word_count}\n"
              f"Specific Word ('{specific_word}') Count: {specific_word_count}\n"
              f"Number Count: {number_count}\n"
              f"Special Character Count: {special_char_count}\n"
              f"Vowel Count: {vowel_count}\n"
              f"Consonant Count: {consonant_count}")
    return result

# Function to handle each client
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(4096).decode('utf-8')
            if message.startswith("BROADCAST:"):
                broadcast_message(message.replace("BROADCAST:", ""))
            elif message.startswith("ANALYZE_TEXT:"):
                data, specific_word = message.replace("ANALYZE_TEXT:", "").split("|")
                result = analyze_text(data, specific_word)
                client_socket.send(f"RESULT:{result}".encode('utf-8'))
            elif message.startswith("ANALYZE_FILE:"):
                data, specific_word = message.replace("ANALYZE_FILE:", "").split("|")
                result = analyze_text(data, specific_word)
                client_socket.send(f"RESULT:{result}".encode('utf-8'))
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to broadcast a message to all clients
def broadcast_message(message):
    for client in clients:
        try:
            client.send(f"BROADCAST:{message}".encode('utf-8'))
        except:
            clients.remove(client)

# Function to start the clients automatically as subprocesses
def start_clients(num_clients):
    for i in range(num_clients):
        print(f"Starting client {i + 1}...")
        subprocess.Popen(['python', 'all_in_one_client.py'])  # Launches client_script.py
        time.sleep(2)  # 2-second delay between each client start

# Server setup
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 50000))
    server.listen()
    print("Server is listening on port 5555...")

    # Ask for the number of clients to launch automatically
    try:
        num_clients = int(input("Enter the number of clients to launch automatically: "))
    except ValueError:
        print("Invalid number. Please enter a valid integer.")
        return

    # Start the specified number of clients
    threading.Thread(target=start_clients, args=(num_clients,)).start()

    while True:
        client_socket, _ = server.accept()
        clients.append(client_socket)
        print("New client connected.")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

# Start the server
start_server()

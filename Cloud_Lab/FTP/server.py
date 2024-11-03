import socket
import threading
import string


# Function to analyze text data
def analyze_text(data, specific_word):
    word_count = len(data.split())
    specific_word_count = data.lower().count(specific_word.lower()) if specific_word != "NONE" else 0
    number_count = sum(c.isdigit() for c in data)
    special_char_count = sum(c in string.punctuation for c in data)
    vowel_count = sum(c in 'aeiouAEIOU' for c in data)
    consonant_count = sum(c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' for c in data)

    # Prepare the analysis result
    result = (f"Word Count: {word_count}\n"
              f"Specific Word ('{specific_word}') Count: {specific_word_count}\n"
              f"Number Count: {number_count}\n"
              f"Special Character Count: {special_char_count}\n"
              f"Vowel Count: {vowel_count}\n"
              f"Consonant Count: {consonant_count}")
    return result


# Handle each client connection
def handle_client(client_socket):
    while True:
        try:
            # Receive data from client
            data = client_socket.recv(4096).decode('utf-8')
            if not data:
                break

            # Receive specific word from client
            specific_word = client_socket.recv(1024).decode('utf-8')

            # Analyze the data
            result = analyze_text(data, specific_word)

            # Send analysis result back to client
            client_socket.send(result.encode('utf-8'))
        except:
            break
    client_socket.close()


# Server setup
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen()
    print("Server is listening on port 5555...")

    while True:
        client_socket, _ = server.accept()
        print("New client connected.")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


# Run the server
start_server()

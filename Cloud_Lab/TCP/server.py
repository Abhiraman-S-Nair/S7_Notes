# TCP Server Code with EXIT functionality
import socket
import threading

# Server address and port
HOST = '127.0.0.1'
PORT = 65432

# Function to handle client messages
def handle_client(conn, addr):
    print(f"[CONNECTED] {addr} connected.")
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message or message.upper() == "EXIT":
                print(f"[DISCONNECTED] {addr} disconnected.")
                break
            print(f"[CLIENT {addr}]: {message}")
            response = input("Enter message to send to client (type 'EXIT' to end): ")
            conn.sendall(response.encode('utf-8'))
            if response.upper() == "EXIT":
                print("[SERVER] Connection closed by server.")
                break
        except:
            print(f"[ERROR] Connection with {addr} ended unexpectedly.")
            break
    conn.close()

# Main server function
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()

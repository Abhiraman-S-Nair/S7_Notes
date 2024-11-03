# TCP Client Code with EXIT functionality
import socket

# Server address and port
HOST = '127.0.0.1'
PORT = 65432


# Connect to server and start chat
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"[CONNECTED] Connected to server at {HOST}:{PORT}")

    while True:
        message = input("Enter message to send to server (type 'EXIT' to end): ")
        client.sendall(message.encode('utf-8'))
        if message.upper() == "EXIT":
            print("[CLIENT] Connection closed by client.")
            break
        response = client.recv(1024).decode('utf-8')
        if response.upper() == "EXIT":
            print("[SERVER] Server closed the connection.")
            break
        print(f"[SERVER]: {response}")

    client.close()


if __name__ == "__main__":
    start_client()

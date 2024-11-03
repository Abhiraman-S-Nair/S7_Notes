# UDP Client Code with EXIT functionality
import socket

# Server address and port
HOST = '127.0.0.1'
PORT = 65432

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"[CONNECTED] Ready to communicate with server at {HOST}:{PORT}")

    while True:
        message = input("Enter message to send to server (type 'EXIT' to end): ")
        client.sendto(message.encode('utf-8'), (HOST, PORT))
        if message.upper() == "EXIT":
            print("[CLIENT] Connection closed by client.")
            break
        data, addr = client.recvfrom(1024)
        response = data.decode('utf-8')
        if response.upper() == "EXIT":
            print("[SERVER] Server closed the connection.")
            break
        print(f"[SERVER]: {response}")

    client.close()

if __name__ == "__main__":
    start_client()

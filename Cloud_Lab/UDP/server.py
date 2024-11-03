# UDP Server Code with EXIT functionality
import socket

# Server address and port
HOST = '127.0.0.1'
PORT = 65432

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        data, addr = server.recvfrom(1024)
        message = data.decode('utf-8')
        if message.upper() == "EXIT":
            print(f"[CLIENT {addr}] Client ended the connection.")
            break
        print(f"[CLIENT {addr}]: {message}")
        response = input("Enter message to send to client (type 'EXIT' to end): ")
        server.sendto(response.encode('utf-8'), addr)
        if response.upper() == "EXIT":
            print("[SERVER] Server ended the connection.")
            break

if __name__ == "__main__":
    start_server()

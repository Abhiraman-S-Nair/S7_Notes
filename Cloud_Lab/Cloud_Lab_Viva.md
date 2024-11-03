# Viva Questions on Sockets and Cloud Computing

## 1. How can sockets be used in cloud-based applications?
Sockets enable communication between clients and servers over a network. In cloud applications, they facilitate real-time data exchange, enabling features like chat services, online gaming, and collaborative tools by maintaining persistent connections.

## 2. How do you create a socket in Python? Provide a basic example.
You can create a socket in Python using the `socket` module. Here’s a basic example of a TCP client:

```python
import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Send data
client_socket.sendall(b'Hello, Server!')

# Close the socket
client_socket.close()
```

## 3. Explain the difference between TCP and UDP sockets.
- **TCP (Transmission Control Protocol):**
  - Connection-oriented protocol.
  - Ensures reliable data transmission, maintaining order and integrity.
  - Suitable for applications like web browsing and file transfers.

- **UDP (User Datagram Protocol):**
  - Connectionless protocol.
  - Faster but does not guarantee reliability, order, or data integrity.
  - Suitable for applications like live streaming and online gaming.

## 4. What are some Python libraries or frameworks that facilitate socket programming in cloud applications?
- **Socket:** The built-in library for socket programming.
- **asyncio:** For asynchronous socket handling.
- **Twisted:** An event-driven networking engine.
- **Django Channels:** For WebSocket support in Django applications.

## 5. How can you implement a basic multi-threaded socket server in Python?
Here’s a simple example of a multi-threaded TCP server:

```python
import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f'Received: {request}')
    client_socket.send(b'ACK')
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(5)

while True:
    client_sock, addr = server.accept()
    print(f'Accepted connection from {addr}')
    client_handler = threading.Thread(target=handle_client, args=(client_sock,))
    client_handler.start()
```

## 6. What is cloud computing?
Cloud computing is the delivery of computing services (servers, storage, databases, networking, software) over the internet ("the cloud"), enabling flexible resources and economies of scale.

## 7. What are the main types of cloud computing services?
- **Infrastructure as a Service (IaaS):** Provides virtualized computing resources over the internet (e.g., AWS EC2).
- **Platform as a Service (PaaS):** Provides a platform allowing customers to develop, run, and manage applications without infrastructure complexity (e.g., Google App Engine).
- **Software as a Service (SaaS):** Delivers software applications over the internet on a subscription basis (e.g., Google Workspace, Salesforce).

## 8. What are some advantages of using cloud computing?
- Cost efficiency: Reduces the need for physical hardware.
- Scalability: Easily scale resources up or down as needed.
- Accessibility: Access services from anywhere with an internet connection.
- Disaster recovery: Improved data backup and recovery options.

## 9. What is a virtual machine (VM)?
A virtual machine is a software-based emulation of a physical computer. It runs an operating system and applications like a physical machine, allowing multiple VMs to operate on a single physical server.

## 10. What is a cloud service provider?
A cloud service provider is a company that offers cloud computing services, including infrastructure, platforms, and software, to individuals and businesses over the internet (e.g., Amazon Web Services, Microsoft Azure).

## 11. What is socket programming?
Socket programming involves using sockets to enable communication between different processes over a network, allowing data exchange in various network protocols (TCP/IP, UDP).

## 12. What are the different types of sockets in Python?
- **Stream Sockets (TCP):** Used for connection-oriented communication.
- **Datagram Sockets (UDP):** Used for connectionless communication.
- **Raw Sockets:** Used for low-level network protocol access (generally not common for application-level programming).

# CDL 411 Cloud Computing Lab Viva Questions & Answers

### 1. What is a network?
- A network is a collection of interconnected devices.
- It enables data sharing and communication.
- Examples include computer networks, telephone networks.
- Networks vary in scope and purpose (e.g., LAN, WAN).
  
### 2. What are the different types of networks?
- **LAN (Local Area Network)**: Covers small areas like a building.
- **MAN (Metropolitan Area Network)**: Covers a city or campus.
- **WAN (Wide Area Network)**: Covers large geographic areas.
- **PAN (Personal Area Network)**: For personal devices, e.g., Bluetooth.
  
### 3. What is the difference between LAN, MAN, and WAN?
- **LAN**: Limited to a building, high speed, low cost.
- **MAN**: Spans cities, moderate speed, medium cost.
- **WAN**: Covers countries/continents, low speed, high cost.
  
### 4. Explain the OSI model and its layers.
- **OSI Model**: Framework to standardize networking.
- **Layers**: Physical, Data Link, Network, Transport, Session, Presentation, Application.
- Each layer has specific functions and protocols.
  
### 5. What is the TCP/IP model? How is it different from the OSI model?
- **TCP/IP Model**: Simplified 4-layer model: Link, Internet, Transport, Application.
- **Difference**: Fewer layers than OSI; widely used on the Internet.

### 6. What is a protocol?
- Rules for communication between network devices.
- Ensures standardized data exchange.
  
### 7. Explain the function of common network protocols like HTTP, FTP, and SMTP.
- **HTTP**: Web data transfer.
- **FTP**: File transfer.
- **SMTP**: Email transfer.

### 8. What is the difference between TCP and UDP?
- **TCP**: Reliable, connection-oriented.
- **UDP**: Unreliable, connectionless, faster.
  
### 9. What is IP addressing? Explain the difference between IPv4 and IPv6.
- **IP Addressing**: Unique identifier for devices on a network.
- **IPv4**: 32-bit, 4.3 billion addresses.
- **IPv6**: 128-bit, vast address space.

### 10. What is a subnet mask? How is it used?
- Divides IP addresses into network/host parts.
- Helps in routing and managing IP ranges.

### 11. What are the different types of network devices?
- **Router**: Directs traffic between networks.
- **Switch**: Connects devices within a network.
- **Hub**: Basic device, broadcasts data to all devices.

### 12. Explain the function of a router, switch, and hub.
- **Router**: Connects multiple networks, routes data.
- **Switch**: Directs data to specific devices.
- **Hub**: Broadcasts data to all devices.

### 13. What is a firewall? How does it work?
- Filters incoming and outgoing network traffic.
- Blocks unauthorized access based on rules.

### 14. What is a gateway?
- Device that connects different networks.
- Translates data formats and protocols.

### 15. What are common network security threats?
- **Malware**: Viruses, Trojans.
- **Phishing**: Deceptive emails/websites.
- **DDoS**: Overloads network.
- **Eavesdropping**: Intercepts data.

### 16. What is encryption? How does it help in network security?
- Converts data into unreadable form.
- Protects data confidentiality.

### 17. Explain the concept of a VPN.
- **VPN (Virtual Private Network)**: Secure, encrypted network over the internet.
- Provides privacy and remote access.

### 18. What are intrusion detection and prevention systems (IDS/IPS)?
- **IDS**: Monitors network for threats.
- **IPS**: Blocks threats in real-time.

### 19. How do you configure a router?
- Access router settings through IP.
- Set up SSID, password, and security protocols.

### 20. What is a MAC address?
- Unique hardware identifier for network interfaces.
- Assigned to each device's network adapter.

### 21. How can you find the IP address of your computer?
- Use `ipconfig` (Windows) or `ifconfig` (Linux/Mac).
- Check network settings in the control panel.

### 22. What tools can you use to troubleshoot network issues?
- **Ping**: Tests connectivity.
- **Traceroute**: Tracks route of data.
- **NSLookup**: Checks DNS configuration.
  
### 23. Explain the use of ping and traceroute commands.
- **Ping**: Checks if a host is reachable.
- **Traceroute**: Shows path data packets take.

### 24. What is DHCP and how does it work?
- **DHCP (Dynamic Host Configuration Protocol)**: Assigns IP addresses dynamically.
- Simplifies network management.

### 25. Explain how DNS works.
- Resolves domain names to IP addresses.
- Uses a hierarchical structure.

---

## Additional Questions

### 1. How do you use the 'ipconfig' command to configure network interfaces in Linux?
- Use `ifconfig` for Linux to configure interfaces.
- `ifconfig eth0 up` to activate interfaces.

### 2. What are the key differences between TCP and UDP?
- **TCP**: Reliable, ordered, error-checked.
- **UDP**: Faster, no ordering, minimal error checking.

### 3. Explain the concept of sliding window protocol.
- Flow control method in TCP.
- Allows multiple packets to be sent before receiving an acknowledgment.

### 4. Explain how routing tables are updated in Distance Vector Routing.
- Routers share their routing tables with neighbors.
- Update paths based on distance metrics.

### 5. How does the leaky bucket algorithm regulate traffic flow?
- Limits data transmission rate.
- Packets enter a buffer (bucket) and leak out at a steady rate.

### 6. How do you use the 'ifconfig' command to configure network interfaces in Linux?
- Configure IP address, netmask, etc., using `ifconfig`.

### 7. Describe the 'socket()' system call and its parameters.
- Used to create a network socket.
- Parameters: domain, type, protocol.

### 8. How does a TCP client establish a connection to a server?
- Uses a three-way handshake (SYN, SYN-ACK, ACK).

### 9. Compare and contrast Distance Vector Routing with Link State Routing.
- **Distance Vector**: Periodic updates, simple.
- **Link State**: Global updates, complex but efficient.

### 10. What are the main challenges faced in implementing sliding window protocols?
- Handling lost packets, acknowledgment delays.
- Balancing window size for optimal throughput.

### 11. Explain how routing tables are updated in Distance Vector Routing.
- **Routers share** their routing tables with neighbors.
- Updates are based on **distance metrics**.
- **Shortest path** selected using Bellman-Ford algorithm.
- Routes are recalculated if network changes occur.
- Simple but may converge slowly.

### 12. Describe the components involved in FTP communication.
- **Client**: Requests file transfer.
- **Server**: Provides requested files.
- **Control connection**: Manages session commands.
- **Data connection**: Handles actual file data.
- Uses **port 21 for control** and **port 20 for data** (by default).

### 13. How does the leaky bucket algorithm regulate traffic flow?
- Packets are added to a **bucket** at arrival.
- Bucket has a **fixed capacity**; excess packets are dropped.
- Packets leave the bucket at a constant rate.
- **Smooths bursty traffic** into a steady flow.
- Used for **traffic shaping** in networks.

### 14. Compare and contrast Distance Vector Routing with Link State Routing.
- **Distance Vector**:
  - Simple, periodic updates.
  - Slower convergence, less complex.
- **Link State**:
  - Faster convergence with global knowledge.
  - Complex, requires more processing power.
- Both used for **dynamic routing** but differ in update methods.

### 15. What are the main challenges faced in implementing sliding window protocols?
- **Window size management** for efficiency.
- Handling **packet loss** and retransmission.
- Dealing with **network delays** and out-of-order packets.
- Ensuring **acknowledgment** of each window.
- Balancing flow control and throughput.


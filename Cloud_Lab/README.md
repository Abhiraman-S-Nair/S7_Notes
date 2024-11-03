# TCP vs. UDP Comparison

| Feature                   | TCP (Transmission Control Protocol)                                         | UDP (User Datagram Protocol)                                    |
|---------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------|
| **History**               | Developed in 1974 by Vint Cerf and Bob Kahn as part of the original IP suite | Introduced in 1980 as a simpler, connectionless alternative to TCP |
| **Protocol Type**         | Connection-oriented                                                       | Connectionless                                                 |
| **Reliability**           | Highly reliable - guarantees delivery, order, and data integrity            | Unreliable - does not guarantee delivery, order, or integrity  |
| **Data Transmission**     | Ensures data packets arrive in the correct order                           | No order is guaranteed; packets may arrive out of order or be lost |
| **Connection**            | Establishes a connection using a three-way handshake (SYN, SYN-ACK, ACK)   | No connection establishment is needed                           |
| **Flow Control**          | Flow control using windowing mechanism                                     | No flow control mechanism                                       |
| **Congestion Control**    | Manages congestion through algorithms (e.g., TCP Reno, TCP Tahoe)          | No congestion control, making it lightweight                    |
| **Error Checking**        | Performs error-checking and retransmits lost packets                       | Performs error-checking but does not retransmit lost packets    |
| **Header Size**           | 20 bytes (due to additional fields for control)                           | 8 bytes (minimal control fields)                                |
| **Overhead**              | High, due to connection setup, sequencing, error correction                | Low, due to minimal error-checking and no connection setup      |
| **Speed**                 | Generally slower, as it prioritizes reliability over speed                 | Faster, as it sends data without waiting for acknowledgments    |
| **Transmission Method**   | Uses streams (data sent as a continuous flow)                             | Uses datagrams (data sent in discrete chunks)                   |
| **Use Cases**             | Applications needing high reliability, such as web pages (HTTP/HTTPS), email, and file transfers (FTP) | Real-time applications needing speed over reliability, such as video streaming, online gaming, VoIP |
| **Advantages**            | Reliable data transfer, ordered packets, error recovery, congestion control | Low latency, simple protocol, low overhead, efficient for real-time data |
| **Disadvantages**         | Higher latency, more complex, more overhead                               | No guarantee of delivery or order, can lose or duplicate packets |
| **Security**              | Supports encryption and authentication in higher layers (e.g., TLS)       | Limited to basic error-checking; security must be handled by higher layers |
| **Connection Termination**| Four-way handshake (FIN, ACK, FIN-ACK, ACK)                               | No termination; each packet is independent                      |
| **Applications**          | HTTP/HTTPS, FTP, SSH, email (SMTP, IMAP, POP)                             | DNS, VoIP, video conferencing, online games, DHCP               |
| **Port Numbers**          | Uses well-known ports such as 80 (HTTP), 443 (HTTPS), 21 (FTP)            | Uses well-known ports such as 53 (DNS), 69 (TFTP), 123 (NTP)    |
| **When to Use**           | Ideal when data accuracy and order are critical                           | Ideal when low latency is prioritized, and some data loss is acceptable |
| **Suitability for Multicasting** | Not suitable for multicast (limited to unicast)                       | Supports multicast, allowing efficient distribution to multiple clients |
| **Data Transmission Control** | Provides mechanisms to control data flow                               | No control mechanisms - simply sends datagrams                   |

---

## Summary

- **TCP** is suitable for applications where data integrity, order, and reliability are crucial. It requires a connection setup and has higher overhead, making it better for tasks like web browsing, file transfers, and emails.
- **UDP** is a lightweight, fast protocol suitable for applications where low latency is essential, and some data loss is acceptable, like video streaming, online gaming, and VoIP.

# TCP and UDP Questions and Answers

## TCP Questions and Answers

1. **What does TCP stand for?**
   - **Answer:** Transmission Control Protocol.

2. **What type of connection does TCP provide?**
   - **Answer:** TCP provides a connection-oriented communication.

3. **Does TCP guarantee data delivery?**
   - **Answer:** Yes, TCP guarantees reliable data delivery through acknowledgments and retransmissions.

4. **What is the maximum segment size (MSS) in TCP?**
   - **Answer:** MSS is the largest segment of data that TCP is willing to receive in a single TCP segment.

5. **How does TCP handle flow control?**
   - **Answer:** TCP uses a sliding window mechanism for flow control, which ensures that a sender does not overwhelm a receiver with too much data.

6. **What is a TCP three-way handshake?**
   - **Answer:** A process that establishes a TCP connection using SYN, SYN-ACK, and ACK packets.

7. **What port number does HTTP use over TCP?**
   - **Answer:** HTTP uses port 80 by default.

8. **Can TCP be used for streaming applications?**
   - **Answer:** Yes, but it may introduce latency due to its reliability mechanisms, which might not be ideal for real-time streaming.

9. **What is TCP segmentation?**
   - **Answer:** TCP segmentation is the process of dividing application data into smaller segments for transmission.

10. **How does TCP ensure data integrity?**
    - **Answer:** TCP uses checksums to verify the integrity of data segments.

11. **What happens if a TCP packet is lost?**
    - **Answer:** The sender will retransmit the lost packet after a timeout period.

12. **Is TCP suitable for applications requiring low latency?**
    - **Answer:** No, because TCP's reliability mechanisms can introduce delays.

13. **What does the TCP state "TIME_WAIT" indicate?**
    - **Answer:** It indicates that a TCP connection has been closed but is waiting to ensure all packets are received before fully closing.

14. **How is TCP different from UDP?**
    - **Answer:** TCP is connection-oriented, provides reliability, and ensures data delivery, while UDP is connectionless, does not guarantee delivery, and has lower latency.

15. **What is the purpose of TCP's flow control?**
    - **Answer:** To prevent a fast sender from overwhelming a slow receiver with data.

16. **What is the role of TCP's sequence numbers?**
    - **Answer:** Sequence numbers are used to order packets and ensure that data is reassembled in the correct order.

17. **What command can you use to see active TCP connections in Linux?**
    - **Answer:** The `netstat` or `ss` command can be used to view active TCP connections.

18. **What is the maximum transmission unit (MTU) in TCP?**
    - **Answer:** MTU is the largest size of a packet that can be sent over a network. For Ethernet, it is typically 1500 bytes.

19. **What does TCP's "urgent" flag do?**
    - **Answer:** The urgent flag signals that certain data within the segment should be prioritized.

20. **What are TCP ports used for?**
    - **Answer:** TCP ports are used to identify specific processes or services running on a host.

---

## UDP Questions and Answers

1. **What does UDP stand for?**
   - **Answer:** User Datagram Protocol.

2. **What type of connection does UDP provide?**
   - **Answer:** UDP provides a connectionless communication.

3. **Does UDP guarantee data delivery?**
   - **Answer:** No, UDP does not guarantee reliable data delivery.

4. **What is the maximum payload size of a UDP packet?**
   - **Answer:** The maximum payload size is 65,507 bytes (including the UDP header).

5. **What is a common use case for UDP?**
   - **Answer:** UDP is commonly used for applications requiring real-time data transmission, such as video streaming and online gaming.

6. **What port number does DNS use over UDP?**
   - **Answer:** DNS uses port 53 by default.

7. **How does UDP handle flow control?**
   - **Answer:** UDP does not implement flow control; it sends packets without ensuring the receiver can handle them.

8. **What happens if a UDP packet is lost?**
   - **Answer:** If a UDP packet is lost, it is not retransmitted, and the application must handle any loss.

9. **What is the structure of a UDP packet?**
   - **Answer:** A UDP packet consists of a header (8 bytes) followed by the payload data.

10. **Is UDP suitable for applications requiring low latency?**
    - **Answer:** Yes, UDP is suitable for low-latency applications since it does not perform error checking and correction.

11. **What does the UDP checksum do?**
    - **Answer:** The UDP checksum is used to detect errors in the transmitted data.

12. **Can UDP support multicasting?**
    - **Answer:** Yes, UDP supports multicasting, allowing a single packet to be sent to multiple destinations.

13. **What is the difference between UDP and TCP in terms of overhead?**
    - **Answer:** UDP has less overhead compared to TCP because it does not maintain a connection or require acknowledgments.

14. **What is the purpose of the source and destination ports in a UDP packet?**
    - **Answer:** They identify the sending and receiving applications on the hosts.

15. **Can a UDP socket be used for bi-directional communication?**
    - **Answer:** Yes, a UDP socket can be used for bi-directional communication, but it does not establish a connection.

16. **What command can you use to send a UDP packet from the command line?**
    - **Answer:** The `nc` (netcat) command can be used to send UDP packets.

17. **What are the advantages of using UDP?**
    - **Answer:** Advantages include lower latency, reduced overhead, and ease of implementation for certain applications.

18. **How does UDP handle packet ordering?**
    - **Answer:** UDP does not guarantee packet ordering; packets may arrive out of order.

19. **What is a common example of a protocol that uses UDP?**
    - **Answer:** The Real-time Transport Protocol (RTP) used for streaming media often runs over UDP.

20. **Can UDP be used over the internet?**
    - **Answer:** Yes, UDP can be used over the internet for applications that do not require guaranteed delivery or ordering.


# Linux Network Commands and Viva Questions

# Linux Network Commands

| Command                   | Description                                                 |
|---------------------------|-------------------------------------------------------------|
| `ifconfig`                | Displays or configures network interface parameters.        |
| `ip addr`                 | Shows IP addresses assigned to all network interfaces.      |
| `ping [hostname/IP]`      | Checks connectivity to a host.                              |
| `traceroute [hostname]`   | Displays the route packets take to reach a network host.    |
| `netstat -tuln`          | Lists all active listening ports and their associated protocols. |
| `ss`                      | Displays socket statistics and can show established connections. |
| `curl [URL]`             | Transfers data from or to a server using various protocols. |
| `wget [URL]`             | Downloads files from the web.                               |
| `scp [source] [user@host:destination]` | Securely copies files between hosts over SSH.        |
| `rsync -avz [source] [destination]` | Synchronizes files/directories between two locations.   |
| `telnet [hostname/IP] [port]` | Connects to a specified port on a remote host.               |
| `nslookup [hostname]`    | Queries DNS to obtain domain name or IP address mapping.   |
| `dig [hostname]`         | Performs DNS lookup and provides detailed information.      |
| `route -n`               | Displays the kernel routing table.                           |
| `ip route`               | Shows or manipulates the IP routing table.                  |
| `iptables -L`            | Lists all current firewall rules.                            |
| `nmap [hostname/IP]`     | Scans networks to discover hosts and services.              |
| `arp -a`                 | Displays the ARP table, showing IP and MAC address mapping. |
| `mtr [hostname]`         | Combines the functionality of `ping` and `traceroute`.     |
| `hostname`                | Displays or sets the system's hostname.                     |
| `whois [domain]`         | Retrieves information about a domain from the WHOIS database. |
| `ifup [interface]`       | Activates a network interface.                              |
| `ifdown [interface]`     | Deactivates a network interface.                            |
| `sudo systemctl restart networking` | Restarts the networking service on the system.      |
| `ethtool [interface]`     | Displays or changes Ethernet device settings.               |
| `ip neigh`               | Displays the ARP table entries.                             |
| `curl -I [URL]`          | Fetches HTTP headers from a web server.                     |

---

## Viva Questions and Answers on Network Commands

1. **What is the purpose of the `ping` command?**
   - **Answer:** `ping` is used to check the reachability of a host on a network by sending ICMP echo requests and measuring the response time.

2. **How do you display the current IP address in Linux?**
   - **Answer:** You can use the `ip addr` command to display the current IP addresses assigned to all network interfaces.

3. **What is the difference between `tcp` and `udp`?**
   - **Answer:** TCP (Transmission Control Protocol) is connection-oriented and provides reliable data transfer, while UDP (User Datagram Protocol) is connectionless and does not guarantee delivery.

4. **How can you check open ports on a server?**
   - **Answer:** You can use the `nmap <hostname>` command to scan a host for open ports and the services running on them.

5. **What command would you use to check the routing table in Linux?**
   - **Answer:** The `route` command can be used to display or modify the IP routing table.

6. **Explain the purpose of `curl`.**
   - **Answer:** `curl` is used to transfer data to or from a server using various protocols, including HTTP, FTP, and more.

7. **What is `ssh` used for?**
   - **Answer:** SSH (Secure Shell) is used to securely log into a remote machine and execute commands.

8. **How do you download a file using `wget`?**
   - **Answer:** You can use the command `wget <url>` to download files from the web non-interactively.

9. **What does the `traceroute` command do?**
   - **Answer:** `traceroute` traces the route that packets take to reach a network host, showing each hop along the way.

10. **How can you list network interfaces in Linux?**
    - **Answer:** You can use the `ip link` command to list all network interfaces and their status.

11. **What is the purpose of the `ftp` command?**
    - **Answer:** The `ftp` command is used to connect to an FTP server to upload or download files.

12. **Explain the significance of the `iptables` command.**
    - **Answer:** `iptables` is used to configure the Linux kernel's packet filtering rules for controlling network traffic.

13. **How do you configure a wireless network interface?**
    - **Answer:** You can use the `iwconfig` command to configure wireless network interfaces and view their settings.

14. **What is `scp` and how is it used?**
    - **Answer:** `scp` (Secure Copy Protocol) is used to securely copy files over SSH between local and remote hosts.

15. **How can you view active network connections?**
    - **Answer:** You can use the `netstat` command to view active network connections and their status.

16. **What is the purpose of `nslookup`?**
    - **Answer:** `nslookup` is used to query DNS to obtain the domain name or IP address mapping.

17. **What does the `mtr` command combine?**
    - **Answer:** `mtr` combines the functionalities of `ping` and `traceroute` to diagnose network connectivity.

18. **How do you check the ARP cache in Linux?**
    - **Answer:** You can use the `arp` command to display or modify the ARP cache, which maps IP addresses to MAC addresses.

19. **What does `ss` command do?**
    - **Answer:** The `ss` command is used to investigate sockets and show more detailed information than `netstat`.

20. **What is the main difference between `telnet` and `ssh`?**
    - **Answer:** `telnet` is an unsecured protocol used for remote connections, while `ssh` provides a secure encrypted connection for remote access.

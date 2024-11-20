# University Term Paper Questions and Answers

## 1. Explain the concept of Single System Image (SSI) in a computing cluster. (3)
1. **Definition**: SSI refers to the abstraction where a cluster appears as a single system to users and applications.
2. **Simplified Management**: Users interact with the system as if it is a single computer, hiding the complexity of the underlying cluster.
3. **Applications**: Commonly used in distributed computing for load balancing and resource management.
4. **Advantages**: Enhances ease of use, improves system scalability, and facilitates centralized control.
5. **Examples**: Used in systems like Beowulf clusters and grid computing.

---

## 2. List the essential features of cloud computing. (3)
1. **On-Demand Self-Service**: Users can provision resources like storage and computing power without human intervention.
2. **Broad Network Access**: Resources are accessible over the internet using standard devices.
3. **Resource Pooling**: Multiple users share resources dynamically based on demand.
4. **Rapid Elasticity**: Resources can be scaled up or down quickly.
5. **Measured Service**: Pay-as-you-go model with usage monitoring and billing.

---

## 3. Mention at least three levels at which virtualization may be implemented. (3)
1. **Hardware Virtualization**: Abstracts physical hardware into virtual machines (e.g., VMware, VirtualBox).
2. **Operating System Virtualization**: Enables multiple OS instances on a single machine (e.g., Docker, LXC).
3. **Application Virtualization**: Runs applications in isolated environments (e.g., Wine, ThinApp).

---

## 4. Is virtualization essential for cloud computing? Explain. (3)
1. **Not Mandatory**: Virtualization is not essential but is highly beneficial for efficient cloud computing.
2. **Resource Optimization**: Virtualization enables efficient resource utilization by allowing multiple VMs on one physical machine.
3. **Isolation**: Provides better security and isolation between users.
4. **Alternatives**: Some clouds use containerization (e.g., Kubernetes) instead of traditional virtualization.

---

## 5. An organization has decided to migrate their IT infrastructure to the cloud. Which are some of the open-source software architectures they can rely on to set up a private cloud environment? (3)
1. **OpenStack**: A popular platform offering flexible and scalable private cloud solutions.
2. **CloudStack**: Provides tools for managing and deploying private clouds.
3. **Eucalyptus**: Allows organizations to build AWS-compatible private clouds.

---

## 6. Name three Software-as-a-Service solutions offered by Google. (3)
1. **Google Workspace**: Includes Gmail, Google Drive, Docs, Sheets, and more.
2. **Google Meet**: For video conferencing and online meetings.
3. **Google Calendar**: For scheduling and event management.

---

## 7. Explain the data types in Pig Latin. (3)
1. **Scalar Types**: Includes simple data types like `int`, `long`, `float`, `double`, `chararray`, and `bytearray`.
2. **Complex Types**: 
   - **Tuple**: Represents a collection of fields.
   - **Bag**: A collection of tuples.
   - **Map**: Key-value pairs for structured data.
3. **Null**: Represents missing or undefined values.

---

## 8. Name the three main types of data to store which, Big Table was developed by Google. (3)
1. **Web Data**: For indexing web pages.
2. **Geographic Data**: Supporting services like Google Earth and Google Maps.
3. **Personal Data**: For user-specific services like Gmail and Google Drive.

---

## 9. Define “trust” in a computer science context. (3)
1. **Definition**: Trust is the expectation that a system or entity behaves as intended under agreed-upon conditions.
2. **Security Context**: Trust determines the level of confidence in authentication, authorization, and data integrity.
3. **Importance**: Crucial for establishing reliable communication and interactions in distributed systems.

---

## 10. Explain the following concepts: (3)
### i. Confidentiality
1. **Definition**: Ensures that information is accessible only to authorized entities.
2. **Mechanisms**: Includes encryption, access control, and authentication.
3. **Purpose**: Protects sensitive data from unauthorized access.

### ii. Integrity
1. **Definition**: Guarantees that data remains unaltered and accurate during transmission or storage.
2. **Mechanisms**: Uses checksums, hashing, and digital signatures.
3. **Purpose**: Prevents tampering and ensures data reliability.

### iii. Availability
1. **Definition**: Ensures that systems, services, and data are accessible when needed.
2. **Mechanisms**: Includes redundant systems, failover, and backup solutions.
3. **Purpose**: Reduces downtime and maintains business continuity.

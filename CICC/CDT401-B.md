# [Detailed Answers to Term Paper Questions](./CDT401-B.pdf)

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

---

Here are the detailed answers for the questions you provided:

---

## 11 a) **Differentiate Grid Computing and Cloud Computing (7)**

1. **Conceptual Difference**:  
   - **Grid Computing**: Focuses on pooling together resources (computational power, storage) from multiple distributed systems to solve complex problems.
   - **Cloud Computing**: Provides on-demand, scalable computing resources and services (e.g., compute, storage) through the internet.

2. **Resource Allocation**:  
   - **Grid Computing**: Resources are typically distributed across multiple locations and managed by different organizations, often with a focus on solving large-scale scientific or academic problems.
   - **Cloud Computing**: Resources are provided by centralized data centers and can be allocated dynamically on demand to users globally.

3. **Management and Control**:  
   - **Grid Computing**: It requires the collaboration of different organizations or institutions, and resources are often controlled by individual organizations.
   - **Cloud Computing**: Centralized control by cloud service providers such as AWS, Azure, or Google Cloud, providing a seamless experience for users.

4. **Scalability**:  
   - **Grid Computing**: Scalability is often limited to the available resources across different organizations, making it less flexible compared to cloud computing.
   - **Cloud Computing**: Highly scalable as resources are virtualized and users can scale their infrastructure up or down depending on demand.

5. **Usage Model**:  
   - **Grid Computing**: Primarily used for resource-intensive tasks like simulations, data analysis, and scientific computations.
   - **Cloud Computing**: Offers a broader range of services including storage, computing power, databases, and networking for various industries.

6. **Cost Model**:  
   - **Grid Computing**: Often relies on public or private grants for funding, and users generally share resources without direct cost models.
   - **Cloud Computing**: Typically follows a pay-as-you-go or subscription-based pricing model, making it more flexible and cost-efficient for businesses.

7. **Security and Compliance**:  
   - **Grid Computing**: Security is a significant challenge because resources are often distributed across different institutions and managed by different administrators.
   - **Cloud Computing**: Cloud service providers offer advanced security features, compliance certifications, and dedicated teams to ensure data privacy and security.

## 11 b) **Discuss the Key Features of Infrastructure as a Service (IaaS) (7)**

1. **On-Demand Resources**:  
   IaaS provides computing resources such as virtual machines, storage, and networking on-demand. Users can quickly provision and scale these resources as needed.

2. **Virtualization Technology**:  
   IaaS relies heavily on virtualization to provide isolated virtual machines and storage systems. This allows users to run their applications without worrying about hardware maintenance.

3. **Pay-As-You-Go Model**:  
   IaaS typically operates on a pay-as-you-go pricing model, where users are charged based on the resources they consume (e.g., storage, CPU, bandwidth), allowing cost flexibility.

4. **Scalability**:  
   IaaS enables dynamic scalability. Users can easily scale their resources (compute power, storage) up or down based on demand, ensuring optimal resource utilization.

5. **Self-Service Portal**:  
   Most IaaS platforms provide a self-service portal or API for users to manage and configure their resources, making it more flexible and user-friendly.

6. **Storage Options**:  
   IaaS provides a range of storage solutions, including block storage, object storage, and file storage, which users can choose based on their needs (e.g., large-scale data storage, databases).

7. **Flexibility and Control**:  
   With IaaS, users have control over the operating systems, applications, and other software configurations. This makes it ideal for businesses that require customized environments.

---

## 12 a) **Write a Note on the Different Computing Practices and Technologies that Lead Up to Cloud Computing (8)**

1. **Mainframe Computing**:  
   In the early stages of computing, organizations used large mainframes to run complex applications. These systems were centralized, with multiple users accessing the machine through terminals.

2. **Client-Server Architecture**:  
   In the 1980s and 1990s, the client-server model emerged, where client machines accessed services and resources hosted on servers. This marked the beginning of distributed computing.

3. **Virtualization**:  
   The advent of virtualization technology in the 1990s allowed for the partitioning of physical servers into multiple virtual machines. Virtualization was crucial in creating the dynamic and scalable environment that cloud computing is built upon.

4. **Grid Computing**:  
   Grid computing emerged as a way to pool resources from multiple computers to solve complex problems. It focused on utilizing underused processing power and storage resources, which laid the groundwork for cloud's resource-sharing model.

5. **Utility Computing**:  
   Utility computing is based on the idea of delivering computing resources as a metered service, similar to utilities like water or electricity. This pay-per-use model directly influenced the development of cloud computing.

6. **Service-Oriented Architecture (SOA)**:  
   SOA, developed in the 1990s, helped to define cloud computing by promoting modular, reusable services that can be accessed over the internet. It was key to the transition towards cloud services.

7. **Broadband and Internet Growth**:  
   The rapid growth of high-speed internet in the 2000s provided the necessary infrastructure for cloud computing to flourish. It enabled businesses to access remote services with minimal latency.

8. **Web 2.0 and SaaS**:  
   The growth of Web 2.0 technologies in the early 2000s led to the rise of Software-as-a-Service (SaaS) offerings like Google Docs and Salesforce. These services demonstrated the potential of cloud computing for businesses and consumers.

## 12 b) **Explain Service Oriented Architecture (SOA) and Discuss How it Applies to Cloud Computing (7)**

1. **Concept of SOA**:  
   Service-Oriented Architecture (SOA) is an architectural design pattern where services are provided to other applications or services through a communication protocol (usually HTTP, SOAP, or REST). Services are loosely coupled and reusable.

2. **Modular Design**:  
   SOA breaks down an application into smaller, independent services that perform specific tasks. This modular approach allows organizations to build complex systems from smaller, reusable components.

3. **Interoperability**:  
   SOA promotes interoperability across different platforms and technologies by defining standard interfaces for services. This is especially important for integrating legacy systems with modern cloud environments.

4. **Loose Coupling**:  
   One of the key principles of SOA is loose coupling. This means that services do not need to know the internal details of other services, making it easier to modify or replace services without impacting the entire system.

5. **Cloud and SOA**:  
   In cloud computing, SOA allows businesses to use different cloud-based services (IaaS, PaaS, SaaS) to build scalable, flexible, and modular applications. This approach aligns well with cloud’s on-demand, scalable model.

6. **Scalability and Flexibility**:  
   SOA enables scaling specific parts of an application rather than scaling the entire system. Cloud providers, like AWS and Azure, use this principle to allow users to scale their infrastructure and services independently.

7. **Agility and Cost Efficiency**:  
   SOA allows businesses to develop applications faster by reusing existing services and adapting to changing requirements. Cloud computing leverages this by providing ready-to-use infrastructure and software, reducing the cost and complexity of managing internal resources.

---

# University Term Paper Questions and Answers

## 1. Illustrate a scenario where the usage of hybrid cloud can be advantageous for an organization? (3)
1. **Data Flexibility**: An e-commerce company uses the private cloud for sensitive payment data and public cloud for managing customer-facing applications during peak traffic.
2. **Cost Efficiency**: A software company runs routine workloads on a private cloud but shifts to public cloud during high demand to save costs.
3. **Disaster Recovery**: A healthcare organization keeps patient records on a private cloud and uses a public cloud for backup and disaster recovery.
4. **Compliance**: A finance firm meets regulatory compliance by storing critical data privately while using the public cloud for analytics.
5. **Scalability**: A media company streams videos on public cloud servers to handle spikes while maintaining an internal database.

---

## 2. Suppose you are a small business owner with computing needs including document editing, presentation and spreadsheet software, storage requirements, etc. Identify the cloud computing service models that you may utilize and mention how they can be utilized. (3)
1. **Software as a Service (SaaS)**: Use Google Workspace or Microsoft 365 for document editing, presentations, and spreadsheets.
2. **Platform as a Service (PaaS)**: Utilize Google App Engine for hosting web-based business applications.
3. **Infrastructure as a Service (IaaS)**: Leverage Amazon S3 or Google Cloud Storage for scalable data storage needs.

---

## 3. Mention the different types of Virtual Machines. (3)
1. **System Virtual Machines**: Provide a complete system environment including a virtualized OS (e.g., VMware, VirtualBox).
2. **Process Virtual Machines**: Run a single application or process in a platform-independent environment (e.g., Java Virtual Machine).
3. **Paravirtual Machines**: Use hypervisor-aware OS for optimized performance in virtualized environments.

---

## 4. Discuss the significance of Domain 0 VM in Xen virtualization environment. (3)
1. **Control VM**: Domain 0 (Dom0) manages other VMs and communicates directly with the hypervisor.
2. **Hardware Access**: Has privileged access to physical hardware and handles I/O requests.
3. **Resource Management**: Allocates system resources like CPU and memory to guest VMs (DomU).
4. **Hypervisor Administration**: Provides the interface for configuring and monitoring the Xen hypervisor.
5. **Security Role**: Acts as a trusted VM, controlling access to system hardware.

---

## 5. An app development company decided to supplement their server structure with available cloud offerings. Name some of the public cloud service providers they can utilize. (3)
1. **Amazon Web Services (AWS)**: Offers scalable and diverse cloud infrastructure.
2. **Microsoft Azure**: Provides tools for app hosting and deployment.
3. **Google Cloud Platform (GCP)**: Focused on analytics and application development.
4. **IBM Cloud**: Known for hybrid cloud solutions.
5. **Oracle Cloud**: Suitable for enterprise application hosting.

---

## 6. Online ticket and token booking applications experience huge variation in customer traffic depending upon the time of the day (e.g., Tatkal booking time in the morning). What kind of cloud resource provisioning is suitable for such situations? (3)
1. **Dynamic Provisioning**: Automatically allocates resources based on real-time demand.
2. **Auto-Scaling**: Increases or decreases server instances as customer traffic varies.
3. **Pay-as-You-Go Model**: Ensures cost efficiency by charging only for used resources.

---

## 7. Explain the purpose of Heartbeat and Blockreport messages. (3)
1. **Heartbeat**: Regular signals sent by DataNodes to the NameNode in Hadoop to indicate they are operational.
2. **Blockreport**: Comprehensive messages from DataNodes to NameNode detailing all data blocks they store.
3. **Purpose**: Ensures data integrity, health monitoring, and fault tolerance within Hadoop clusters.

---

## 8. Name at least three online calendar applications. (3)
1. **Google Calendar**: Integrated with Google Workspace and popular for scheduling.
2. **Microsoft Outlook Calendar**: Suitable for business and enterprise environments.
3. **Apple Calendar**: A built-in solution for Apple ecosystem users.
4. **Zoho Calendar**: A versatile calendar for personal and professional use.

---

## 9. Provide an outline of the Trusted Computing Base (TCB) concept. (3)
1. **Definition**: TCB comprises the hardware, software, and firmware essential for enforcing a system's security policy.
2. **Purpose**: Ensures the secure execution of critical operations like authentication and data protection.
3. **Components**: Includes elements like operating systems, processors, and trusted software modules.
4. **Role**: Acts as a foundation to prevent breaches and unauthorized access.
5. **Evaluation**: Security evaluations assess the integrity of the TCB.

---

## 10. Write a note on Security-as-a-Service. (3)
1. **Definition**: Security-as-a-Service (SECaaS) provides security solutions via the cloud.
2. **Features**: Includes firewalls, intrusion detection, antivirus, and endpoint protection.
3. **Benefits**: Reduces infrastructure costs, simplifies updates, and ensures scalability.
4. **Examples**: Services like Symantec Cloud, McAfee SECaaS, and AWS Security Hub.
5. **Use Cases**: Ideal for businesses needing flexible and comprehensive security frameworks.

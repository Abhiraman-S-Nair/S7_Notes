
# Notes on Apache Spark and Hadoop

## 1. Overview

**Apache Spark**:
- An open-source distributed computing system designed for big data processing.
- Provides high-level APIs in Java, Scala, Python, and R.
- Features in-memory data processing for faster performance compared to traditional disk-based processing.

**Hadoop**:
- An open-source framework for distributed storage and processing of large datasets across clusters of computers.
- Based on the MapReduce programming model.
- Consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce.

## 2. Components of Hadoop

1. **Hadoop Distributed File System (HDFS)**:
   - A distributed file system designed to run on commodity hardware.
   - Provides high throughput access to application data.
   - Data is stored in blocks (default 128MB or 256MB) across the cluster.
   - Features replication (default replication factor is 3) for fault tolerance.

2. **MapReduce**:
   - A programming model for processing large data sets.
   - Consists of two main functions: Map (processes and converts input data into key-value pairs) and Reduce (aggregates the results).
   - Handles parallel processing and data distribution.

3. **YARN (Yet Another Resource Negotiator)**:
   - Resource management layer of Hadoop.
   - Manages and schedules resources in the cluster.
   - Separates resource management from data processing, allowing multiple data processing engines to run.

4. **Hadoop Common**:
   - The common utilities and libraries that support other Hadoop modules.
   - Provides file system and operating system abstractions.

## 3. Components of Apache Spark

1. **Spark Core**:
   - The foundation of Spark, providing the basic functionalities like task scheduling, memory management, and fault recovery.
   - Supports in-memory computing for fast data processing.

2. **Spark SQL**:
   - Module for structured data processing.
   - Provides a programming interface for working with structured and semi-structured data using SQL queries.
   - Integrates with various data sources like HDFS, Apache Hive, and Apache HBase.

3. **Spark Streaming**:
   - Enables processing of real-time data streams.
   - Supports various data sources, including Kafka, Flume, and HDFS.
   - Provides windowed computations and stateful processing.

4. **MLlib**:
   - Spark's machine learning library.
   - Offers various machine learning algorithms and utilities for classification, regression, clustering, and recommendation.
   - Scalable to big data applications.

5. **GraphX**:
   - Spark's API for graph processing.
   - Provides a set of graph algorithms and utilities for building and transforming graphs.

## 4. Applications

- **Hadoop**:
  - Data storage and processing for big data analytics.
  - Batch processing of large datasets.
  - ETL processes in data warehousing.
  - Log processing and analysis.

- **Spark**:
  - Real-time data processing for streaming applications.
  - Interactive data analysis using Spark SQL.
  - Machine learning and data science projects using MLlib.
  - Graph processing and analysis with GraphX.

# Viva Questions on Apache Spark and Hadoop

### 1. What is Hadoop?
Hadoop is an open-source framework that allows for the distributed processing of large datasets across clusters of computers using a simple programming model called MapReduce.

### 2. What are the main components of Hadoop?
The main components of Hadoop are HDFS (Hadoop Distributed File System), MapReduce, YARN (Yet Another Resource Negotiator), and Hadoop Common.

### 3. What is HDFS?
HDFS is a distributed file system that stores data across multiple machines, providing high throughput access to application data and fault tolerance through data replication.

### 4. Explain the MapReduce programming model.
MapReduce is a programming model that processes large data sets by dividing tasks into two main functions: Map, which processes input data and generates key-value pairs, and Reduce, which aggregates the results.

### 5. What is YARN?
YARN is the resource management layer of Hadoop that manages and schedules resources in the cluster, allowing for multiple data processing engines to run simultaneously.

### 6. What is Apache Spark?
Apache Spark is an open-source distributed computing system that provides fast data processing with high-level APIs and in-memory computing capabilities.

### 7. What are the components of Apache Spark?
The main components of Apache Spark include Spark Core, Spark SQL, Spark Streaming, MLlib (machine learning library), and GraphX (graph processing API).

### 8. What is the role of Spark SQL?
Spark SQL is a module for structured data processing that allows users to run SQL queries against structured and semi-structured data, providing integration with various data sources.

### 9. Explain Spark Streaming.
Spark Streaming is a component of Spark that enables processing of real-time data streams, allowing for data ingestion from sources like Kafka and Flume, and performing computations on the data as it arrives.

### 10. What is MLlib?
MLlib is Spark's machine learning library that provides scalable algorithms and utilities for machine learning tasks, such as classification, regression, clustering, and collaborative filtering.

### 11. What is GraphX?
GraphX is Spark's API for graph processing that provides a set of graph algorithms and tools for building and transforming graphs.

### 12. How does Spark achieve fault tolerance?
Spark achieves fault tolerance through its RDD (Resilient Distributed Dataset) abstraction, which automatically tracks data lineage and can recompute lost data in the event of a failure.

### 13. What is in-memory computing in Spark?
In-memory computing is a feature of Spark that allows data to be processed in RAM, significantly speeding up data access times compared to disk-based systems like Hadoop MapReduce.

### 14. Can Spark run on top of Hadoop?
Yes, Spark can run on top of Hadoop, leveraging HDFS for storage and YARN for resource management.

### 15. What is the difference between batch processing and stream processing?
Batch processing handles large volumes of data that are processed in chunks at specific intervals, while stream processing handles continuous data streams in real-time.

### 16. What is data locality in Hadoop?
Data locality refers to the ability of a computing framework to perform computations as close to the data as possible to reduce data transfer times and increase processing efficiency.

### 17. What are the advantages of using Spark over Hadoop?
Spark offers faster processing speeds due to in-memory computing, supports real-time data processing, provides a rich set of APIs for various data operations, and is easier to use with higher-level abstractions.

### 18. What is a Spark RDD?
RDD (Resilient Distributed Dataset) is a fundamental data structure in Spark that represents an immutable distributed collection of objects that can be processed in parallel.

### 19. How does Spark handle data partitioning?
Spark automatically partitions data across the cluster based on the number of available nodes and allows users to control partitioning using transformations.

### 20. What are some common applications of Spark?
Common applications of Spark include data analysis, machine learning, real-time data processing, ETL processes, and interactive analytics in big data environments.

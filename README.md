Introduction
This part of the project demonstrates how to set up our real-time data processing pipeline using Docker, Kafka, and Spark. The pipeline ingests data from a CSV file (`nyc-taxi-data.csv`), streams it into Kafka, and processes it using Spark Structured Streaming.
Docker Compose
Docker Compose is a tool for defining and running multi-container Docker applications. For this project, a `docker-compose.yml` file was created to define the services required: Kafka, ZooKeeper, and Spark.
 

Components:
•	ZooKeeper: A centralized service for maintaining configuration information and providing distributed synchronization. It's a critical dependency for Kafka, which uses it for managing distributed brokers.
•	Kafka: A distributed streaming platform used for building real-time data pipelines. It is designed to handle high volumes of data. In this project, Kafka ingests the `nyc-taxi-data.csv` file and serves as a buffer for real-time data.
•	Spark (Master and Worker): A distributed computing system that processes data in real-time. In this setup, both the Spark master and worker nodes are deployed. The master coordinates the distribution of data and computation tasks to the workers.
Why Docker?
Using Docker Compose makes it easy to start, scale, and manage the different components of our pipeline. It ensures that the services run in isolation, with their required dependencies, in a consistent environment. This approach simplifies deployment, scaling, and operations.
 

Data Ingestion: Kafka Producer
A Python script was created to read the `nyc-taxi-data.csv` file and produce (send) its records to a Kafka topic named `nyc-taxi-data`. Kafka serves as the streaming platform, allowing Spark to consume the data in real-time.
 
 

Data Processing: Spark Structured Streaming
Once the data is in Kafka, Spark Structured Streaming is used to consume and process it in real-time. The Spark job connects to the Kafka topic, reads the incoming data, transforms it from a raw string into structured data (DataFrames), and then performs desired computations or transformations. 
 
 


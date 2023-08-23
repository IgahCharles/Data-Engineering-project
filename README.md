# Project Overview
In today's data-driven world, organizations deal with vast amounts of data that require efficient processing and analysis. To tackle this challenge, a batch-processing-based data architecture can provide a scalable and reliable solution. 
The objective of this project is to design and implement a robust batch-processing data architecture for a data-intensive machine learning application. The architecture will have the capabilities to ingest vast amounts of data, store it efficiently, and preprocess and aggregate the data for seamless integration with the machine learning application. In this phase, I will cover an in-depth exploration of selected software components, architectural design, data source, and a visual represent the proposed system architecture.

## Architecture Overview
The batch-processing-based data architecture is designed to handle large volumes of data in regular intervals or batches. This project consists of Six (6) layers, which are as follows:

### Data Source
Dataset Name: New York City Taxi Trip Duration
Source: Kaggle
Link to Dataset: https://www.kaggle.com/c/nyc-taxi-trip-duration/data      
This dataset includes details of over 1.45 million taxi trips in New York City. It includes data points such as pickup time, drop-off time, trip duration, passenger count, pickup longitude, pickup latitude, drop-off longitude, and drop-off latitude.
The main points of interest for this project are the pickup time (timestamp) and the trip duration. The large number of data points and the presence of a timestamp make this dataset a suitable option.

#### Potential Uses:
This data can be used to study patterns in taxi usage, trip durations, traffic patterns based on trip durations and times, etc. It could be of particular interest to traffic management studies, urban planning, and ride-hailing services optimization.

### Data Ingestion Layer
The data ingestion layer focuses on efficiently capturing and transferring the incoming data to the processing pipeline. It consists of the following several microservices:      
•	Event Streaming: For this project, I will be using Apache Kafka which is used to handle real-time data streaming and queuing. The reason for this is that it ensures fault-tolerant, scalable, and reliable ingestion of data from multiple sources.
•	Batch Processing: For this, I will use Apache Spark which enables the processing of large volumes of data in batch mode. 

# Getting Started
## Prerequisites
+ Docker and Docker Compose installed
+ Git

## Steps:
1. Clone the repository:   
git clone https://github.com/IgahCharles/Data-Engineering-project.git   
cd Data-Engineering-project

2. Spin up the Docker services:
   
   docker-compose up -d
4. Ingest the data into Kafka:
   Execute the provided Python script to read nyc-taxi-data.csv and produce its records to the Kafka topic.
   
   python producer.py
   
5. Process the data with Spark:      
Execute the provided PySpark script to consume and process the data from the Kafka topic.

spark-submit --packages org.apache.spark:spark-sql-kafka-0-10:<spark_version> consumer.py

   


 


 
 


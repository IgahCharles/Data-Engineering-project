from kafka import KafkaProducer
import csv

# Define the Kafka producer with the appropriate bootstrap server
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Open the CSV file
with open('nyc-taxi-data.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header
    next(reader, None)
    
    # Send each row to the Kafka topic
    for row in reader:
        producer.send('nyc-taxi-data', ','.join(row).encode('utf-8'))

# Close the producer
producer.close()

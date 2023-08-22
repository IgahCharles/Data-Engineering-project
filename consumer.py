from kafka import KafkaConsumer

# Define the Kafka consumer with the appropriate bootstrap server and group id
consumer = KafkaConsumer(
    'nyc-taxi-data',
    bootstrap_servers='localhost:9092',
    group_id='nyc-taxi-group',
    auto_offset_reset='earliest',  # Start from the beginning of the topic
    value_deserializer=lambda x: x.decode('utf-8')  # Decode messages using utf-8
)

# Print each message from the Kafka topic
for message in consumer:
    print(message.value)

# Close the consumer (optional, as the loop will run indefinitely)
consumer.close()

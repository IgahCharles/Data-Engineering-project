from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Kafka-Spark-Integration") \
    .getOrCreate()

# Read from Kafka
kafkaStream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "nyc-taxi-data") \
    .load()

# Deserialize the value from Kafka message
kafkaStream = kafkaStream.selectExpr("CAST(value AS STRING) as value")

# Write the stream to console
query = kafkaStream.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()

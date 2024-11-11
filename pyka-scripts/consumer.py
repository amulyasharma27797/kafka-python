import json

from kafka import KafkaConsumer


if __name__ == "__main__":

    # Instantiating the Kafka Consumer
    consumer = KafkaConsumer(
        "registered_user",  # Name of the Topic
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='earliest',  # Telling consumer from where to pick the message  
        group_id="consumer-group-a"
    )

    print("Starting the consumer")

    # Printing the messages received on the consumer
    for msg in consumer:
        print(f"Registered User: {json.loads(msg.value)}")

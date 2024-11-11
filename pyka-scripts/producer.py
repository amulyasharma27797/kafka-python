import json
import os
import time
from kafka import KafkaProducer

from data import get_registered_user


# Get Kafka bootstrap server from environment variable
bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')


def json_serializer(data: dict) -> str:
    """
    Defining a JSON serialiser in order 
    to send the serialised data to Kafka Topic.
    Data must be serialised before being sent to a topic.
    :param data: dict
    :return: str
    """
    return json.dumps(data).encode('utf-8')
 

def get_partition(key_bytes, all_parititions, available_partitions) -> int:
    """
    This method is used to return the paritiion number 
    (in case of multiple partitions) to which we want 
    to send the message to the topic on Kafka.
    :param key_bytes:
    :param all_partitions: 
    :param available_partitions:
    :return: int
    """
    return 0
    

# Creating a producer with Docker-Kafka IP Address
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=json_serializer,
    # partitioner=get_partition
)


# Running the program with a registered user
if __name__ == "__main__":
    while 1 == 1:
        # Getting the registered user details
        registered_user = get_registered_user()
        print(registered_user)

        # Passing the topic name
        producer.send("registered_user", registered_user)

        # Delay for 4 seconds after every message being sent
        time.sleep(4)

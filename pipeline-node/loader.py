from confluent_kafka import Consumer, KafkaException
import json

# Configure consumer
consumer_conf = {
    'bootstrap.servers': 'redpanda:9092',
    'group.id': 'loader-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe(['threat-updates-ecs'])

def load_message(transformed_message):
    #TODO load the messages into the database after developing schema
    """
    Load a transformed message.

    Args:
        transformed_message (dict): The transformed message to be loaded.

    Returns:
        None

    This function takes a transformed message as input and prints it. In a real-world scenario,
    it would load the data into a storage system. The message is formatted as a JSON string
    with an indent of 2 for readability.

    Example usage:
    ```
    transformed_message = {
        "key": "value",
        "another_key": "another_value"
    }
    load_message(transformed_message)
    ```
    """
    
    print(f"Loading message: {json.dumps(transformed_message, indent=2)}")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        transformed_message = json.loads(msg.value().decode('utf-8'))
        load_message(transformed_message)
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

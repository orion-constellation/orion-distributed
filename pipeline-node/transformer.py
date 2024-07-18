from confluent_kafka import Consumer, Producer, KafkaException
import json
import pyarrow as pa

# Configure consumer
consumer_conf = {
    'bootstrap.servers': 'redpanda:9092',
    'group.id': 'transformer-group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe(['threat-updates'])

# Configure producer
producer_conf = {'bootstrap.servers': 'redpanda:9092'}
producer = Producer(producer_conf)

def ensure_ecs_format(raw_message):
    """
    Ensures that the given `raw_message` is in the Elastic Common Schema (ECS) format.
    
    Args:
        raw_message (dict): The raw message to be transformed into the ECS format.
        
    Returns:
        dict: The transformed message in the ECS format.
        
    The ECS format is a standardized way of representing log data. It includes the following fields:
    
    - '@timestamp' (str): The timestamp of the event in ISO 8601 format. If the `raw_message` does not have a '@timestamp' field, the current timestamp is used.
    - 'event' (dict): The event information. It includes the following fields:
        - 'category' (str): The category of the event. Defaults to 'threat'.
        - 'type' (str): The type of the event. Defaults to the value of the 'threat_type' field in the `raw_message`, or 'unknown' if it is not present.
    - 'threat' (dict): The threat information. It includes the following fields:
        - 'framework' (str): The framework used for the threat. Defaults to 'MITRE ATT&CK'.
        - 'technique' (str): The technique used in the threat. Defaults to the value of the 'technique' field in the `raw_message`, or 'unknown' if it is not present.
        - 'id' (str): The ID of the threat. Defaults to the value of the 'id' field in the `raw_message`, or 'unknown' if it is not present.
        - 'name' (str): The name of the threat. Defaults to the value of the 'name' field in the `raw_message`, or 'unknown' if it is not present.
    - 'host' (dict): The host information. It includes the following fields:
        - 'hostname' (str): The hostname of the host. Defaults to the value of the 'hostname' field in the `raw_message`, or 'unknown' if it is not present.
        - 'ip' (str): The IP address of the host. Defaults to the value of the 'ip' field in the `raw_message`, or 'unknown' if it is not present.
    """
    return {
        '@timestamp': raw_message.get('@timestamp', pa.timestamp('ms').now().as_py().isoformat() + 'Z'),
        'event': raw_message.get('event', {
            'category': 'threat',
            'type': raw_message.get('threat_type', 'unknown')
        }),
        'threat': raw_message.get('threat', {
            'framework': 'MITRE ATT&CK',
            'technique': raw_message.get('technique', 'unknown'),
            'id': raw_message.get('id', 'unknown'),
            'name': raw_message.get('name', 'unknown')
        }),
        'host': raw_message.get('host', {
            'hostname': raw_message.get('hostname', 'unknown'),
            'ip': raw_message.get('ip', 'unknown')
        })
    }

def delivery_report(err, msg):
    """
    Prints a delivery report for a message.

    Args:
        err (Exception): An exception object if the message delivery failed, or None if it succeeded.
        msg (Message): The message that was delivered or attempted to be delivered.

    Returns:
        None

    This function checks if the `err` argument is not None. If it is not None, it prints a message indicating that the message delivery failed, along with the error message. If `err` is None, it prints a message indicating that the message was delivered to the specified topic and partition.

    """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

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
        raw_message = json.loads(msg.value().decode('utf-8'))
        transformed_message = ensure_ecs_format(raw_message)
        producer.produce('threat-updates-ecs', key=msg.key(), value=json.dumps(transformed_message), callback=delivery_report)
        producer.flush()
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    producer.flush()

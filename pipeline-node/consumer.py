from confluent_kafka import Consumer, KafkaException
import json

conf = {
    'bootstrap.servers': 'redpanda:9092',
    'group.id': 'threat-group',
    'auto.offset.reset': 'earliest'
}

c = Consumer(conf)

c.subscribe(['threat-updates'])

def process_threat(threat_message):
    """
    Process a threat message by printing it in a formatted way.

    Args:
        threat_message (dict): A dictionary representing the threat message.

    Returns:
        None

    This function takes a threat message as input and prints it in a formatted way. The threat message is first converted to a JSON string using the `json.dumps()` function with an indentation of 2 spaces. The resulting string is then printed to the console using the `print()` function.

    Example:
        >>> threat_message = {"type": "malware", "name": "Trojan.Win32.Agent.Nyx", "description": "This is a malicious trojan that can steal sensitive information."}
        >>> process_threat(threat_message)
        Processing threat: {
          "type": "malware",
          "name": "Trojan.Win32.Agent.Nyx",
          "description": "This is a malicious trojan that can steal sensitive information."
        }
    """
    print(f"Processing threat: {json.dumps(threat_message, indent=2)}")

try:
    while True:
        msg = c.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        process_threat(json.loads(msg.value().decode('utf-8')))
except KeyboardInterrupt:
    pass
finally:
    c.close()
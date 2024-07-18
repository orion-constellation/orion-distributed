from confluent_kafka import Producer
import json
import time
import pyarrow as pa

def delivery_report(err, msg):
    """
    A function that handles the delivery report of a message.

    Parameters:
    err (str): The error message if the message delivery failed.
    msg (str): The message object that was delivered.

    Returns:
    None
    """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

p = Producer({'bootstrap.servers': 'redpanda:9092'})

while True:
    message = {
        '@timestamp': pa.timestamp('ms').now().as_py().isoformat() + 'Z',
        'event': {
            'category': 'threat',
            'type': 'malware'
        },
        'threat': {
            'framework': 'MITRE ATT&CK',
            'technique': 'T1059',
            'id': 'malware-sample-id',
            'name': 'Sample Malware'
        },
        'host': {
            'hostname': 'node1',
            'ip': '192.168.1.1'
        }
    }
    p.produce('threat-updates', key='node1', value=json.dumps(message), callback=delivery_report)
    p.flush()
    time.sleep(10)

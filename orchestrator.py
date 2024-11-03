# orchestrator.py
import json
import pika  # RabbitMQ client for Python
import requests

# Configuration and Message Queue settings
QUEUE_NAME = 'task_queue'
RABBITMQ_HOST = 'localhost'

# Load configuration dynamically (from a central config store)
def load_configuration(country_operator_pair):
    response = requests.get(f'https://config-store.com/{country_operator_pair}')
    return response.json()

# Send task to the message queue
def send_task(country_operator_pair, program_id):
    config = load_configuration(country_operator_pair)
    task = {
        'program_id': program_id,
        'country_operator': country_operator_pair,
        'config': config
    }
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        body=json.dumps(task),
        properties=pika.BasicProperties(delivery_mode=2)  # make message persistent
    )
    print(f" [x] Sent task for {country_operator_pair}")
    connection.close()

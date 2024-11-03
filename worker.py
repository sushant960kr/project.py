# worker.py
import json
import pika
import time
import threading
from ratelimit import limits, sleep_and_retry

QUEUE_NAME = 'task_queue'
RABBITMQ_HOST = 'localhost'

# Rate limit (e.g., 10 calls per minute)
@sleep_and_retry
@limits(calls=10, period=60)
def execute_program(task):
    program_id = task['program_id']
    country_operator = task['country_operator']
    config = task['config']
    print(f"Executing program {program_id} for {country_operator} with config: {config}")
    # Simulate task execution
    time.sleep(2)

def callback(ch, method, properties, body):
    task = json.loads(body)
    try:
        execute_program(task)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Error executing task: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

def worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    print("Worker started. Waiting for tasks...")
    channel.start_consuming()

# Run multiple worker threads for concurrency
for _ in range(5):
    threading.Thread(target=worker).start()

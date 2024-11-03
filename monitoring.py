# monitoring.py
from prometheus_client import start_http_server, Counter, Summary

# Start a Prometheus HTTP server to expose metrics
start_http_server(8000)

# Define Prometheus metrics
TASK_EXECUTION_TIME = Summary('task_execution_seconds', 'Time spent processing a task')
TASK_FAILURES = Counter('task_failures_total', 'Total number of task failures')

@TASK_EXECUTION_TIME.time()
def execute_task_with_metrics(task):
    try:
        # Here, call execute_program() from worker.py or other task function
        pass  # Insert execution logic
    except Exception as e:
        TASK_FAILURES.inc()  # Increment failure counter
        print(f"Error during execution: {e}")

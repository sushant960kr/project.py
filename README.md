This system efficiently manages six Python programs, executing them dynamically for various country-operator pairs. It leverages RabbitMQ for messaging, Prometheus for monitoring, and Flask as a mock configuration service.

Architecture

Core Components
1. Task Orchestrator - Initiates tasks based on configurations.
2. Message Broker (RabbitMQ) - Manages task queues, rate limiting, and concurrency.
3. Worker Nodes - Autoscaled containers to execute Python programs.
4. Configuration Management (Flask) - Provides dynamic configurations for each task.
5. Monitoring (Prometheus) - Logs metrics for real-time monitoring.
6. Process Management (Docker Compose/Kubernetes) - Manages containerized services


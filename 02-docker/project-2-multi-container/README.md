# Docker Project 2 — Multi-Container Application

## Objective

Build and run a multi-container application using Docker networking and Docker Compose.

The application contains:

- Flask — backend application
- Redis — data store used for the visitor counter

## Architecture

```text
Browser
   ↓
localhost:5000
   ↓
Flask Container
   ↓
Docker Network
   ↓
Redis Container
   ↓
Visitor Count Response
```

Architecture diagram: `archirecture-diagram.png`

## Project Structure

```text
docker-project-2/
├── Dockerfile
├── app.py
├── requirements.txt
├── docker-compose.yml
├── archirecture-diagram.png
└── README.md
```

## Method 1 — Manual Docker

Build the Flask image:

```bash
docker build -t docker-project-2:v1 .
```

Create a Docker network:

```bash
docker network create docker-project-2-network
```

Run Redis:

```bash
docker run -d --name redis --network docker-project-2-network redis
```

Run Flask:

```bash
docker run -d --name flask-app --network docker-project-2-network -p 5000:5000 docker-project-2:v1
```

Verify:

```bash
docker ps
docker network inspect docker-project-2-network
```

Access the application at `http://localhost:5000`.

## Method 2 — Docker Compose

Start both services:

```bash
docker compose up -d
```

Verify:

```bash
docker compose ps
```

Stop the application:

```bash
docker compose down
```

Docker Compose creates the application network and manages the Flask and Redis services together.

## Docker Networking

Flask communicates with Redis using the container name:

```text
redis:6379
```

Redis does not require host port mapping because it is accessed internally by Flask through the Docker network.

## Port Mapping

```text
Host Port 5000 → Container Port 5000
```

The application is accessed through:

```text
http://localhost:5000
```

## Key Concepts Demonstrated

- Docker images
- Docker containers
- Dockerfile
- Docker bridge networks
- Container-to-container communication
- Port mapping
- Flask container
- Redis container
- Docker Compose
- Multi-container application management

## Result

A Flask + Redis multi-container application was successfully run using both manual Docker networking and Docker Compose. The Flask application communicates with Redis and displays an incrementing visitor count.

## Project Status

Completed ✅

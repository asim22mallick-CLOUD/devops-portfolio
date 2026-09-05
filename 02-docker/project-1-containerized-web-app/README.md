# Docker Project 1 — Containerized Web Application

## Objective

Containerize a simple HTML web application using Docker and Nginx.

## Architecture

```text
Browser → Docker Host → Docker Container → Nginx → index.html
```

## Project Structure

```text
docker-project-1/
├── Dockerfile
├── index.html
└── README.md
```

## Dockerfile

The image is based on `nginx:latest`. The HTML page is copied into Nginx's default web root and port 80 is exposed. fileciteturn17file0

## Build the Image

Generic syntax:

```bash
docker build -t <image-name>:<tag> <build-context>
```

Command used:

```bash
docker build -t docker-project-1:v1 .
```

## Run the Container

Generic syntax:

```bash
docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>:<tag>
```

Command used:

```bash
docker run -d -p 80:80 --name docker-project-1-container docker-project-1:v1
```

## Verify

```bash
docker ps
```

Expected port mapping:

```text
0.0.0.0:80->80/tcp
```

Access the application at:

```text
http://localhost
```

## Port Mapping

```text
HOST_PORT:CONTAINER_PORT

80:80
```

Flow:

```text
Host Port 80 → Container Port 80 → Nginx → index.html
```

## Useful Docker Commands

```bash
docker images
docker ps
docker ps -a
docker stop docker-project-1-container
docker start docker-project-1-container
docker rm docker-project-1-container
docker rmi docker-project-1:v1
```

## Skills Learned

- Docker
- Dockerfile
- Docker images
- Docker containers
- Nginx
- Docker build
- Docker run
- Port mapping
- Container lifecycle
- Docker troubleshooting

## Result

The HTML web application was successfully containerized using Docker and Nginx and accessed through the browser.

## Project Status

Completed ✅

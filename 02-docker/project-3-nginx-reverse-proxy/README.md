# Docker Project 3 — Nginx Reverse Proxy

## Objective

Build a multi-container Docker application where Nginx acts as a reverse proxy and routes requests to multiple backend containers.

## Architecture

```text
Browser
   |
   | HTTP :80
   v
Nginx Reverse Proxy
   |
   | Docker Network
   +----> App 1 Container
   |
   +----> App 2 Container
```

The browser communicates only with Nginx. Nginx routes `/app1/` and `/app2/` to the appropriate backend containers.

## Project Structure

```text
docker-project-3/
├── app1.html
├── app2.html
├── Dockerfile.app1
├── Dockerfile.app2
├── Dockerfile.nginx
├── nginx.conf
├── docker-compose.yml
└── README.md
```

## Manual Docker Approach

Build App 1:

```bash
docker build -f Dockerfile.app1 -t docker-project-3-app1:v1 .
```

Build App 2:

```bash
docker build -f Dockerfile.app2 -t docker-project-3-app2:v1 .
```

Create the network:

```bash
docker network create docker-project-3-network
```

Run App 1 and App 2 on the network:

```bash
docker run -d --name app1 --network docker-project-3-network docker-project-3-app1:v1
docker run -d --name app2 --network docker-project-3-network docker-project-3-app2:v1
```

Build the Nginx reverse proxy image:

```bash
docker build -f Dockerfile.nginx -t docker-project-3-nginx:v2 .
```

Run Nginx:

```bash
docker run -d --name nginx-proxy --network docker-project-3-network -p 80:80 docker-project-3-nginx:v2
```

## Nginx Routing

```nginx
location /app1/ {
    proxy_pass http://app1/;
}

location /app2/ {
    proxy_pass http://app2/;
}
```

The trailing slash in `proxy_pass` ensures the URL prefix is removed when forwarding requests to the backend.

## Testing

App 1:

```text
http://localhost/app1/
```

App 2:

```text
http://localhost/app2/
```

## Docker Compose

The same architecture can be managed with Docker Compose:

```bash
docker compose up -d
docker compose ps
```

Stop the application:

```bash
docker compose down
```

## Troubleshooting

A 404 routing issue was diagnosed using:

```bash
docker logs nginx-proxy
```

The issue was caused by incorrect Nginx `location` and `proxy_pass` configuration. Adding trailing slashes corrected the routing, after which the Nginx image was rebuilt and redeployed.

## Skills Learned

- Docker images and containers
- Docker networking
- Nginx reverse proxy
- URL-based routing
- Container-to-container communication
- Port mapping
- Docker Compose
- Container logs and troubleshooting
- Rebuilding and redeploying containers

## Project Status

Completed ✅

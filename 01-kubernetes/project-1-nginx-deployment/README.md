# Kubernetes Project 1 — Nginx Application Deployment

This project demonstrates deploying, managing, scaling, and exposing a containerized Nginx web application using Kubernetes.

## Architecture

![Kubernetes Project 1 Architecture](architecture-diagram.png)

```text
Browser
   │
   │ HTTP :30080
   ▼
AWS EC2 Kubernetes Node
   │
   ▼
NodePort Service :30080
   │
   ▼
Deployment
   │
   ▼
ReplicaSet
   ├── Nginx Pod 1
   └── Nginx Pod 2
```

## Technologies

- Kubernetes
- kubectl
- Nginx
- Docker
- AWS EC2
- AWS Security Groups

## Kubernetes Resources

- Namespace: `nginx-project`
- Deployment: `nginx-deployment`
- Initial replicas: `2`
- Container image: `nginx:latest`
- Service: `nginx-service`
- Service type: `NodePort`
- NodePort: `30080`

## Deployment

The Deployment manifest creates two Nginx replicas and exposes container port 80. fileciteturn4file0L2-L5

## Service

The NodePort Service selects the Nginx Pods and maps port 80 to NodePort 30080. fileciteturn5file0L2-L5

## Scaling

The application was scaled from 2 replicas to 4 replicas:

```bash
kubectl scale deployment nginx-deployment --replicas=4 -n nginx-project
kubectl get pods -n nginx-project
```

## Rolling Update

```bash
kubectl set image deployment/nginx-deployment nginx=<new-image> -n nginx-project
kubectl rollout status deployment/nginx-deployment -n nginx-project
```

## Access

After allowing TCP port `30080` in the AWS EC2 Security Group, the application can be accessed at:

```text
http://<EC2-public-ip>:30080
```

## Verification

```bash
kubectl get all -n nginx-project
kubectl get pods -n nginx-project
kubectl get deployments -n nginx-project
kubectl get replicasets -n nginx-project
kubectl get services -n nginx-project
```

## Outcome

The Nginx application was successfully deployed on Kubernetes, exposed externally through NodePort, scaled from two to four replicas, and updated using a rolling-update strategy.

# Kubernetes Project 1 — Nginx Application Deployment

## 📌 Overview

This project demonstrates how to deploy, manage, scale, and expose a containerized Nginx web application using Kubernetes.

The application is deployed with a Kubernetes Deployment, initially running two replicas, and exposed outside the Kubernetes cluster using a NodePort Service on port `30080`.

The project also demonstrates Kubernetes scaling and rolling updates.

## 🏗️ Architecture

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
   │
   ├── Nginx Pod 1
   └── Nginx Pod 2

AWS Security Group → TCP 30080
```

## 🛠️ Technologies Used

- Kubernetes
- kubectl
- Nginx
- Docker
- AWS EC2
- AWS Security Groups

## ☸️ Kubernetes Components

- **Namespace:** Organizes and isolates project resources.
- **Deployment:** Manages the Nginx application and desired replica count.
- **ReplicaSet:** Maintains the required number of Pods.
- **Pods:** Run the Nginx containers.
- **NodePort Service:** Exposes the application outside the cluster.

## 🚀 Implementation

### 1. Create Namespace

```bash
kubectl create namespace <namespace-name>
kubectl get namespaces
```

### 2. Deploy Nginx

```bash
kubectl apply -f deployment.yaml
kubectl get deployments -n <namespace-name>
```

### 3. Verify Pods and ReplicaSet

```bash
kubectl get pods -n <namespace-name>
kubectl get replicasets -n <namespace-name>
```

The initial deployment runs two Nginx replicas.

### 4. Create NodePort Service

```bash
kubectl apply -f service.yaml
kubectl get service -n <namespace-name>
```

The application is exposed through NodePort `30080`.

### 5. Configure AWS Security Group

Allow inbound TCP traffic on port `30080` to the EC2 Kubernetes node. For production environments, access should be restricted to the required IP ranges rather than `0.0.0.0/0`.

### 6. Access the Application

```text
http://<EC2-public-ip>:30080
```

The Nginx welcome page should be displayed.

## 📈 Scaling

The application was initially deployed with two replicas and then scaled to four replicas:

```bash
kubectl scale deployment <deployment-name> --replicas=4 -n <namespace-name>
kubectl get pods -n <namespace-name>
```

This demonstrates horizontal scaling at the Kubernetes Deployment level.

## 🔄 Rolling Update

The project also demonstrates updating the Nginx container image without taking the whole application offline.

```bash
kubectl get deployment <deployment-name> -n <namespace-name> -o jsonpath='{.spec.template.spec.containers[0].image}'

kubectl set image deployment/<deployment-name> <container-name>=<new-image> -n <namespace-name>

kubectl rollout status deployment/<deployment-name> -n <namespace-name>
```

Kubernetes gradually replaces the old Pods with new Pods during the rollout.

## 🔍 Verification Commands

```bash
kubectl get all -n <namespace-name>
kubectl get pods -n <namespace-name>
kubectl get deployments -n <namespace-name>
kubectl get replicasets -n <namespace-name>
kubectl get services -n <namespace-name>
kubectl describe pod <pod-name> -n <namespace-name>
kubectl describe deployment <deployment-name> -n <namespace-name>
```

## 📂 Source Project Structure

```text
kubernetes-project-1-application-deployment/
├── README.md
├── deployment.yaml
├── service.yaml
└── architecture-diagram.png
```

## 🎯 Key Concepts Demonstrated

- Kubernetes Namespace
- Deployment
- ReplicaSet
- Pods
- Services
- NodePort
- Application scaling
- Rolling updates
- Kubernetes networking
- AWS EC2
- AWS Security Groups
- Containerized application deployment

## 💡 What I Learned

This project provided practical experience deploying and managing a containerized application with Kubernetes. It covered how Deployments and ReplicaSets maintain application Pods, how Services provide connectivity, and how NodePort exposes an application outside the cluster.

It also provided hands-on experience with scaling, rolling updates, resource verification, and AWS networking configuration.

## 🏁 Outcome

The Nginx web application was successfully deployed on Kubernetes and exposed externally through a NodePort Service. The application was scaled from two to four replicas, and a rolling update was performed to demonstrate Kubernetes application update capabilities.

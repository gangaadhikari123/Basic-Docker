# 🐳 Docker Complete Guide

Docker allows you to package an application along with all its dependencies into containers, ensuring that the application runs consistently across different environments.

Instead of saying:

> "It works on my machine."

Docker makes sure:

> "It works everywhere."

---

# Table of Contents

* [What is Docker?](#what-is-docker)
* [How Docker Works](#how-docker-works)
* [Docker Architecture](#docker-architecture)
* [Docker Components](#docker-components)
* [Docker Images and Containers](#docker-images-and-containers)
* [Common Docker Commands](#common-docker-commands)
* [Docker Volumes](#docker-volumes)
* [Docker Networks](#docker-networks)
* [Dockerfile](#dockerfile)
* [Docker Compose](#docker-compose)
* [Example Project Structure](#example-project-structure)
* [Useful Docker Commands](#useful-docker-commands)
* [Docker Best Practices](#docker-best-practices)
* [Docker Roadmap](#docker-roadmap)

---

# What is Docker?

Docker is a containerization platform that packages:

* Application code
* Dependencies
* Libraries
* Runtime environment

into lightweight containers.

Containers are:

* Portable
* Isolated
* Fast
* Reproducible

---

# How Docker Works

```text
Application Code
       ↓
Dockerfile
       ↓
Docker Image
       ↓
Docker Container
```

### Step 1: Write Your Application

Examples:

* Django
* Flask
* Node.js
* React
* Spring Boot

---

### Step 2: Create a Dockerfile

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
```

---

### Step 3: Build Docker Image

```bash
docker build -t myapp .
```

This creates an image named:

```text
myapp
```

---

### Step 4: Run a Container

```bash
docker run -p 8000:8000 myapp
```

Access application:

```text
http://localhost:8000
```

---

# Docker Architecture

```text
                Docker Engine
                     │
        ┌────────────┴────────────┐
        │                         │
     Images                  Containers
        │                         │
        └────────────┬────────────┘
                     │
                 Volumes
                     │
                 Networks
```

---

# Docker Components

| Component      | Description                      |
| -------------- | -------------------------------- |
| Dockerfile     | Instructions to build an image   |
| Image          | Blueprint/template               |
| Container      | Running instance of an image     |
| Volume         | Persistent data storage          |
| Network        | Communication between containers |
| Docker Compose | Manage multiple containers       |
| Registry       | Store and share images           |

---

# Docker Images and Containers

### Image

Blueprint of your application.

Example:

```bash
python:3.12
postgres:17
redis:8
nginx:latest
```

---

### Container

Running instance of an image.

```bash
docker run postgres:17
```

---

# Common Docker Commands

## Images

Show images:

```bash
docker images
```

Build image:

```bash
docker build -t myapp .
```

Remove image:

```bash
docker rmi image_id
```

---

## Containers

Run container:

```bash
docker run myapp
```

Run in detached mode:

```bash
docker run -d myapp
```

Run with port mapping:

```bash
docker run -p 8000:8000 myapp
```

List running containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

Stop container:

```bash
docker stop container_id
```

Start container:

```bash
docker start container_id
```

Restart container:

```bash
docker restart container_id
```

Remove container:

```bash
docker rm container_id
```

---

# Logs

View logs:

```bash
docker logs container_id
```

Follow logs:

```bash
docker logs -f container_id
```

---

# Execute Commands Inside Container

Using Bash:

```bash
docker exec -it container_id bash
```

Using sh:

```bash
docker exec -it container_id sh
```

---

# Docker Volumes

Volumes preserve data even after containers are removed.

Create volume:

```bash
docker volume create myvolume
```

List volumes:

```bash
docker volume ls
```

Inspect volume:

```bash
docker volume inspect myvolume
```

Delete volume:

```bash
docker volume rm myvolume
```

---

# Docker Networks

Show networks:

```bash
docker network ls
```

Create network:

```bash
docker network create mynetwork
```

Inspect network:

```bash
docker network inspect mynetwork
```

Remove network:

```bash
docker network rm mynetwork
```

---

# Dockerfile

Think:

> How would I manually set up my application on a fresh machine?

Example:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Dockerfile:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
```

---

# Dockerfile Instructions

### FROM

Base image.

```dockerfile
FROM python:3.12
```

---

### WORKDIR

Working directory.

```dockerfile
WORKDIR /app
```

---

### COPY

Copy files.

```dockerfile
COPY . .
```

---

### RUN

Execute commands while building.

```dockerfile
RUN pip install -r requirements.txt
```

---

### EXPOSE

Expose ports.

```dockerfile
EXPOSE 8000
```

---

### CMD

Container startup command.

```dockerfile
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
```

---

# Docker Compose

Docker Compose manages multiple containers.

Think:

> How do all services work together?

---

## Example: Django + PostgreSQL

```yaml
services:
  backend:
    build: .
    ports:
      - "8000:8000"

  db:
    image: postgres:17
```

---

## React + Node + PostgreSQL

```yaml
services:
  frontend:
    build: ./frontend

  backend:
    build: ./backend

  db:
    image: postgres:17
```

---

## Django + Redis + Celery + PostgreSQL

```text
backend
postgres
redis
celery
```

---

# Docker Compose Commands

Start services:

```bash
docker compose up
```

Background mode:

```bash
docker compose up -d
```

Rebuild images:

```bash
docker compose up --build
```

Stop containers:

```bash
docker compose down
```

Show logs:

```bash
docker compose logs
```

Follow logs:

```bash
docker compose logs -f
```

Show running services:

```bash
docker compose ps
```

Restart services:

```bash
docker compose restart
```

---

# Example Project Structure

```text
project/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── app/
└── .dockerignore
```

---

# Example docker-compose.yml

```yaml
services:
  backend:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app

  db:
    image: postgres:17
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password

  pgadmin:
    image: dpage/pgadmin4
    ports:
      - "5050:80"
```

---

# .dockerignore

Similar to `.gitignore`.

Example:

```text
venv/
.env
__pycache__/
.git
node_modules
```

---

# Useful Cleanup Commands

Remove stopped containers:

```bash
docker container prune
```

Remove unused images:

```bash
docker image prune
```

Remove unused volumes:

```bash
docker volume prune
```

Remove everything unused:

```bash
docker system prune -a
```

---

# Docker Best Practices

### Use Specific Versions

Good:

```dockerfile
FROM python:3.12
```

Avoid:

```dockerfile
FROM python:latest
```

---

### Use .dockerignore

Prevents unnecessary files from being copied.

---

### Keep Images Small

Prefer:

```dockerfile
python:3.12-slim
```

instead of:

```dockerfile
python:3.12
```

---

### Use Environment Variables

Example:

```yaml
environment:
  DEBUG=False
```

---

### Avoid Running as Root

Create non-root users inside containers for production.

---

# Docker Roadmap

## Beginner

* Images
* Containers
* Docker CLI
* Dockerfile

---

## Intermediate

* Volumes
* Networks
* Docker Compose
* Environment Variables
* Multi-container Applications

---

## Advanced

* Multi-stage Builds
* Health Checks
* Bind Mounts
* Named Volumes
* Build Cache
* Docker Registry
* Docker Hub

---

## Expert

* Nginx + Gunicorn + Django
* Redis + Celery
* Reverse Proxy
* Docker Swarm
* Kubernetes
* CI/CD with GitHub Actions
* Monitoring and Logging

---

# Final Goal

Be able to containerize and deploy applications such as:

* Django REST Framework
* React
* Node.js
* PostgreSQL
* Redis
* Celery
* Nginx
* FastAPI
* Microservices Architecture

and eventually orchestrate them using Kubernetes.

# Python Quotes Fetcher

This project fetches daily quotes from a public API and stores them in a PostgreSQL database. It uses Python for the application logic, Docker for containerization, and Kubernetes for orchestration.

## Features

- Fetches random quotes from [Quotable API](https://api.quotable.io/random).
- Stores quotes in a PostgreSQL database.
- Configurable using a `.ini` configuration file.
- Dockerized for easy deployment.
- Kubernetes manifests for cloud deployment.

## Prerequisites

- Docker
- Docker Compose
- Kubernetes (e.g., Minikube, GKE)
- Helm (optional, for Kubernetes deployment)

## Project Structure

app/ ├── Dockerfile ├── docker-compose.yml ├── config.ini ├── app.py ├── Chart.yaml ├── values.yaml └── templates/ ├── app-deployment.yaml ├── app-service.yaml ├── postgres-deployment.yaml └── postgres-service.yaml

bash


## Setup

### Local Development with Docker Compose

1. Clone the repository:
   ```bash
   git clone https://github.com/theprivilegeduser/random.git
   cd app

    Build and run the application with Docker Compose:

    bash

    docker-compose up

    The application will be running on localhost:80.

Deployment on Kubernetes

    Build the Docker image:

    bash

docker build -t theprivilegeduser/random .

Apply the Kubernetes manifests:

bash

    kubectl apply -f templates/postgres-deployment.yaml
    kubectl apply -f templates/postgres-service.yaml
    kubectl apply -f templates/app-deployment.yaml
    kubectl apply -f templates/app-service.yaml

    The application will be accessible via the service created.

Configuration

Edit the config.ini file to change the API URL or database connection settings.

ini

[API]
url = https://api.quotable.io/random

[DATABASE]
url = postgres://user:password@database:5432/quotesdb

Logging

The application logs error messages related to fetching data or database interactions. Check the console output for logs.
License

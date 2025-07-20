Hajarat Busola Akande
Project Overview
This project is a full-stack To-Do Application built with a focus on modern DevOps practices, containerization, and automation. It leverages Docker, Docker Compose, GitHub Actions, Kubernetes, and Terraform to streamline development, deployment, and infrastructure management.

🚀 Key Features
Frontend & Backend Dockerization
The application is split into two services: a frontend (React) and a backend (Node.js/Express), each containerized for consistency across environments.

Docker Compose for Local Development
Easily spin up the entire application with one command using docker-compose.yaml.

CI/CD with GitHub Actions
Automated workflows located in .github/workflows handle code building, testing, and deployment.

Infrastructure as Code (IaC) with Terraform
Cloud infrastructure is managed declaratively using Terraform.

Kubernetes Deployment
Kubernetes manifests are available for deploying the application in a production-grade environment. Service account tokens are securely handled with automountServiceAccountToken: false.

Code Quality Assurance
Integrated static code analysis via SonarQube using the sonar-project.properties file.

🐳 Docker Compose
To simplify local development and testing, the project uses Docker Compose to orchestrate multiple containers (frontend, backend, and optionally a database) in a single development environment.

🔧 What It Does
Docker Compose enables:

Custom Image Builds
Builds Docker images for both frontend and backend services using their respective Dockerfiles.

Service Orchestration
Runs all necessary services (frontend, backend, and optional database) together with a single command:

docker-compose up --build

Inter-Container Networking
Services communicate over a shared Docker network using container names (e.g., frontend calls backend via http://backend:5000).

Port Mapping for Access
Maps container ports to localhost:

Frontend: http://localhost:3000

Backend API: http://localhost:5000

Startup Dependency Management
Ensures containers start in the correct order using depends_on.

Consistent Dev Environment
Removes the need to install dependencies locally. Developers can code, test, and debug directly in containers.

 Getting Started with Docker Compose
Clone the Repository

git clone https://github.com/Hajixhayjhay/DevOps-Class.git

Run the App

docker-compose up --build
Access the Services

Frontend: http://localhost:3000

Backend: http://localhost:5000


# To-Do Application – DevOps Project

**Author:** *Saudat Bada-Akande*

## 📌 Project Overview

This is a full-stack **To-Do Application** designed with a strong emphasis on modern **DevOps practices**, **containerization**, and **automation**. The project utilizes **Docker**, **Docker Compose**, **GitHub Actions**, **Kubernetes**, and **Terraform** to streamline the development workflow, deployment pipeline, and infrastructure provisioning.

---

## 🚀 Key Features

### 🔧 Frontend & Backend Containerization

* The application is split into two main services:

  * **Frontend**: React
  * **Backend**: Node.js with Express
* Each service is containerized to ensure consistency across environments.

### 🐳 Docker Compose for Local Development

* Use a single command to spin up the entire stack, including frontend, backend, and optionally a database.
* Configured via `docker-compose.yaml`.

### 🔁 CI/CD with GitHub Actions

* Automated workflows in `.github/workflows/` handle:

  * Code building
  * Testing
  * Deployment

### ☁️ Infrastructure as Code (IaC) with Terraform

* Cloud infrastructure is provisioned and managed declaratively using **Terraform**.

### ☸️ Kubernetes Deployment

* Kubernetes manifests are provided for deploying the application to a production-grade cluster.
* Secure configurations include `automountServiceAccountToken: false` to enhance security.

### ✅ Code Quality Assurance

* Integrated **static code analysis** using **SonarQube** via the `sonar-project.properties` configuration.

---

## 🐳 Docker Compose Setup

### What Docker Compose Does

* **Builds custom Docker images** for frontend and backend services using individual Dockerfiles.
* **Orchestrates services** to run in a shared environment:

  ```bash
  docker-compose up --build
  ```
* **Enables inter-container communication** using service names (e.g., `http://backend:5000`).
* **Maps container ports** to localhost for easy access:

  * Frontend: [http://localhost:3000](http://localhost:3000)
  * Backend API: [http://localhost:5000](http://localhost:5000)
* **Manages startup order** with `depends_on` to ensure services start in the correct sequence.
* **Creates a consistent development environment**, removing the need for local dependency installation.

---

## 🏁 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/saude27/DevOps-Class.git
cd DevOps-Class
```

### 2️⃣ Run the Application

```bash
# Build and start services
docker-compose up --build

# Alternatively, run in detached mode
docker-compose up -d
```

### 3️⃣ Access the Services

* Frontend: [http://localhost:3000](http://localhost:3000)
* Backend API: [http://localhost:5000](http://localhost:5000)





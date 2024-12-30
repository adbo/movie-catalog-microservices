# Movie Recommendation Service (Work in Progress)

**Project Status: Under Development**

This project is currently under active development and serves as a portfolio piece to demonstrate my skills in building microservices-based applications using Python, FastAPI, Docker, AWS cloud services, and GitHub Actions for CI/CD. While not fully feature-complete, it showcases the core architectural concepts and my ability to integrate various technologies in a microservices environment.

## Overview

The Movie Recommendation Service is a simple application designed to provide a catalog of movies and offer personalized movie recommendations to users. The application is built using a microservices architecture, where different functionalities are separated into independent, deployable services.

**Key Demonstrations (Currently Implemented or Planned):**

* **Microservices Architecture:**  Dividing the application into distinct services with specific responsibilities.
* **Python & FastAPI:**  Utilizing FastAPI for building fast and efficient RESTful APIs for each microservice.
* **Containerization with Docker:** Packaging each microservice into Docker containers for consistent deployment.
* **Cloud Deployment on AWS:**  Planning deployment and management of services on AWS using services like ECS/Fargate (or equivalent).
* **CI/CD with GitHub Actions:** Implementing automated build, test, and deployment pipelines.
* **API Gateway:**  Using an API Gateway (potentially built with FastAPI or AWS API Gateway) as the single entry point for the application.

## Planned Features

As this project is a work in progress, the following features are planned for implementation:

* **Movie Catalog Service (`movie-service`):**
    *  [ ] Basic API endpoints for retrieving movie details.
    *  [ ] Functionality to add, update, and delete movies (admin panel or API endpoints).
    *  [ ] Search functionality based on title, genre, and other criteria.
    *  [ ] Integration with a persistent database (e.g., PostgreSQL).
* **Recommendation Service (`recommendation-service`):**
    *  [ ] Implementation of a basic recommendation algorithm (e.g., collaborative filtering, content-based).
    *  [ ] API endpoint to retrieve movie recommendations for a user.
    *  [ ] Potentially integrating user preferences or viewing history.
* **API Gateway (`api-gateway`):**
    *  [ ] Basic routing of requests to the appropriate microservices.
    *  [ ] Potential implementation of authentication and authorization.
* **Infrastructure as Code (IaC):**
    *  [ ] Using tools like Terraform or CloudFormation to define and manage the AWS infrastructure.
* **Monitoring and Logging:**
    *  [ ] Integrating basic monitoring and logging solutions.

**[X] Indicates features that are currently implemented or partially implemented.**

## Technologies Used

* **Programming Language:** Python
* **API Framework:** FastAPI
* **Containerization:** Docker, Docker Compose
* **Cloud Provider:** Amazon Web Services (AWS)
* **CI/CD:** GitHub Actions
* **Database (Planned for `movie-service`):** PostgreSQL (or similar)
* **Message Broker (Potentially for inter-service communication):**  [To be decided]
* **Other Libraries/Tools:** [List any other relevant libraries used, e.g., SQLAlchemy]

## Getting Started (Local Development - Work in Progress)

Instructions for setting up the project locally will be added as the development progresses. Currently, the focus is on building the core functionalities of the microservices.

**Planned Local Setup Steps:**

1. **Clone the repository:** `git clone [repository-url]`
2. **Navigate to the project directory:** `cd movie-recommendation-service`
3. **Build and run the services using Docker Compose:** `docker-compose up --build`
4. **Access the API Gateway at:** `[Localhost address and port]`

**Note:**  These steps are subject to change as the project evolves.

## Planned AWS Deployment

The project is intended to be deployed on AWS, leveraging services such as:

* **Elastic Container Service (ECS) or Fargate:** For container orchestration.
* **Relational Database Service (RDS):** For the `movie-service` database.
* **ElastiCache (potentially):** For caching or the `recommendation-service`.
* **API Gateway:**  As the entry point for the application.
* **Other relevant AWS services.**

The specific AWS deployment configuration will be documented as the deployment phase is approached.

## CI/CD Pipeline

A GitHub Actions workflow will be implemented to automate the following:

* Building Docker images for each microservice.
* Running unit tests and integration tests.
* Pushing Docker images to a container registry (e.g., Docker Hub or AWS ECR).
* Deploying changes to the AWS environment.

The workflow configuration will be available in the `.github/workflows` directory.

## Contribution

As this is primarily a portfolio project, direct contributions are not expected at this time. However, feedback and suggestions are always welcome.

## Disclaimer

This project is under development and is intended to showcase my skills and understanding of microservices architecture and related technologies. It may not be production-ready or fully optimized.

**Last Updated:** [30 Dec 2024]
Used Python FASTAPI client to make frontend
Folder: fast_api_frontend

Command to run 
"cd  composed-app && docker compose up"


**12-factor app methodology **
**1. Codebase**
Approach:
A single codebase is maintained in version control (e.g., Git).
Your project structure is divided into distinct services: fast_api_frontend, springboot_backend, and database, adhering to modular architecture.
**2. Dependencies**
Approach:
Frontend: Dependencies are specified in requirements.txt (e.g., fastapi, uvicorn, etc.).
Backend: Dependencies are managed in pom.xml (Spring Boot).
Both services use Docker, which ensures isolated environments with dependencies baked into container images.
**3. Config**
Approach:
Configuration is separated from the codebase using environment variables, as seen in the docker-compose.yaml file:
SPRING_DATASOURCE_URL, SPRING_DATASOURCE_USERNAME, and SPRING_DATASOURCE_PASSWORD for the Spring Boot backend.
SPRING_BOOT_API_URL for the FastAPI frontend.
The configuration is injected at runtime, ensuring environment-specific details are decoupled from the code.
**4. Backing Services**
Approach:
Postgres is treated as a backing service, defined as dbpostgres in docker-compose.yaml.
The connection to the database is externalized using environment variables and accessed via service names in Docker (dbpostgres).
**5. Build, Release, Run**
Approach:
Build: Each service is containerized with its Dockerfile.
Release: Docker images are versioned (delcyd/frontend-fastapi:latest, maeddes/backendspringboot:hft24).
Run: Containers are orchestrated with Docker Compose to ensure consistency across environments.
**6. Processes**
Approach:
The application consists of stateless processes.
Backend and frontend services are independently scalable.
Persistent data (e.g., Postgres database) is managed via volumes (postgres-data).
**7. Port Binding**
Approach:
Explicit port bindings are used in docker-compose.yaml:
7000:7000 for FastAPI.
8080:8080 for Spring Boot.
5432:5432 for Postgres.
Each service is self-contained and exposes necessary ports.
**8. Concurrency**
Approach:
Horizontal scaling is supported:
Multiple instances of the frontend or backend can be launched and load-balanced.
Statelessness ensures scalability without code changes.
**9. Disposability**
Approach:
Containers are disposable:
Restart policies in Docker Compose ensure fault tolerance.
Graceful termination is ensured by adhering to container lifecycle best practices.
**10. Dev/Prod Parity**
Approach:
Docker ensures consistency between development, staging, and production environments.
Developers use the same images and configurations as in production.
**11. Logs**
Approach:
Logs are streamed to standard output and captured by Docker.
External log aggregation tools (e.g., ELK Stack) can be integrated if necessary.
**12. Admin Processes**
Approach:
Admin tasks, such as database migrations or seed scripts, can be executed via temporary containers.
Spring Boot and FastAPI allow endpoints for health checks or management tasks.
This structured approach ensures that your project adheres to modern best practices, making it scalable, maintainable, and portable across environments.


🐳 Python Docker Communication ProjectThis project demonstrates a professional DevOps workflow for containerized applications. It features a Client-Server architecture running in isolated environments using Docker.📋 Table of ContentsPrerequisitesNetwork SetupBuilding ImagesRunning ContainersCleanup & Optimization🛠 PrerequisitesDocker Desktop installed and running.Basic understanding of Python and Terminal.1. Network SetupIn Docker, containers are isolated by default. To allow them to communicate, we create a virtual bridge network.# Create a dedicated network for our services
docker network create my-devops-network
2. Building ImagesWe turn our source code into immutable Images. This ensures the "It works on my machine" problem is solved.# Build the Server Image
docker build -t my-server-image ./server

# Build the Client Image
docker build -t my-client-image ./client
3. Running ContainersNow we instantiate our images into running Containers.Step A: Start the Server (Background)The server needs to run in "Detached" mode (-d) so it can listen for requests without blocking the terminal.docker run -d \
  --name my-server \
  --network my-devops-network \
  -p 8000:8000 \
  my-server-image
Step B: Start the Client (Interactive)The client runs in the foreground to show us the logs and the connection result.docker run \
  --name my-client \
  --network my-devops-network \
  my-client-image
🧹 Cleanup & OptimizationAs per Cost Optimization best practices, we must ensure no unused resources are left running.# Stop and remove all project containers
docker rm -f my-server my-client

# Remove the virtual network
docker network rm my-devops-network
DevOps Tip: Always run the cleanup commands after your testing phase to save system RAM and CPU.Created by Yonatan - DevOps Journey 2024
Python Docker Project
This project demonstrates communication between two Python-based services (Client and Server) running inside Docker containers using a custom network.

Create a Docker Network:
To allow containers to communicate using their service names, create a bridge network

Build the Images:
Build the Server image:
docker build -t my-server-image ./server
Build the Client image:
docker build -t my-client-image ./client

Run the Containers:
Run Server (Exposing port 8000 to host):
docker run -d --name my-server --network my-devops-network -p 8000:8000 my-server-image
Run Client:
docker run --name my-client --network my-devops-network my-client-image



    # 🐳 Python Docker Project

This project demonstrates communication between two Python-based services (**Client** and **Server**) running inside Docker containers using a custom network.

---

## 📌 Project Overview

* Two services:

  * **Server** – exposes an API on port `8000`
  * **Client** – communicates with the server using its container name
* Uses a custom Docker bridge network for internal communication

---

## ⚙️ Prerequisites

Make sure you have installed:

* Docker
* Python (optional, for local testing)

---

## 🌐 Create Docker Network

To allow containers to communicate using their service names, create a bridge network:

```bash
docker network create my-devops-network
```

---

## 🏗️ Build Docker Images

### Build Server Image

```bash
docker build -t my-server-image ./server
```

### Build Client Image

```bash
docker build -t my-client-image ./client
```

---

## ▶️ Run Containers

### Run Server (Expose port 8000)

```bash
docker run -d \
  --name my-server \
  --network my-devops-network \
  -p 8000:8000 \
  my-server-image
```

### Run Client

```bash
docker run \
  --name my-client \
  --network my-devops-network \
  my-client-image
```

---

## 🔗 How It Works

* Both containers are connected to the same Docker network
* The client communicates with the server using:

  ```
  http://my-server:8000
  ```
* Docker DNS resolves the container name automatically

---

## 📁 Project Structure

```
.
├── client/
│   └── Dockerfile
├── server/
│   └── Dockerfile
└── README.md
```

---

## ✅ Notes

* Make sure the server is running before starting the client
* You can stop containers using:

```bash
docker stop my-server my-client
```

---

## 🚀 Future Improvements (Optional)

* Add Docker Compose
* Add logging
* Add health checks
* Add tests

---

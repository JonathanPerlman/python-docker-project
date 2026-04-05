# 🐳 Python Docker mTLS Project

This project demonstrates secure communication between two Python-based services (**Client** and **Server**) using **HTTPS with Mutual TLS (mTLS)** inside Docker containers.

---

## 📌 Project Overview

* Two services:

  * **Server** – exposes an HTTPS API on port `8000`
  * **Client** – connects securely using mTLS
* Uses a custom Docker bridge network
* Implements **Mutual TLS authentication**:

  * Client verifies Server
  * Server verifies Client

---

## 📁 Project Structure

```
.
├── client/
│   ├── app.py
│   ├── Dockerfile
│   ├── client.crt
│   ├── client.key
│   └── server.crt
├── server/
│   ├── app.py
│   ├── Dockerfile
│   ├── server.crt
│   ├── server.key
│   └── client.crt
└── README.md
```

---

## ⚙️ Prerequisites

* Docker installed
* Basic understanding of networking (optional)

---

## 🌐 Create Docker Network

```bash
docker network create my-devops-network
```

### ❗ Why?

Allows containers to communicate using container names (DNS resolution).

### 📚 Research Task

* What is DNS?
* How does Docker use internal DNS for container communication?

---

## 🏗️ Build Docker Images

```bash
docker build -t my-server-image ./server
docker build -t my-client-image ./client
```

---

## ▶️ Run Containers

### Run Server

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

* Both containers are on the same network
* Client connects to:

```
https://my-server:8000
```

* Docker resolves `my-server` automatically

---

## 🔐 HTTPS & mTLS Explanation

### What is HTTPS?

HTTPS encrypts communication using TLS to prevent interception.

### What is mTLS?

Mutual TLS means **both sides authenticate each other**:

* Client verifies Server identity
* Server verifies Client identity

---

### 📜 Certificates Usage

#### Client Side:

* `server.crt` → verifies server identity
* `client.crt + client.key` → identifies the client

#### Server Side:

* `server.crt + server.key` → identifies the server
* `client.crt` → verifies client identity

---

## 🔧 Generate Certificates (Self-Signed)

### Generate Server Certificate

```bash
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes
```

### Generate Client Certificate

```bash
openssl req -x509 -newkey rsa:2048 -keyout client.key -out client.crt -days 365 -nodes
```

---

## 🧱 Important: Docker Images Explained

* A Docker Image is a **snapshot of your code**
* Code changes will NOT affect running containers

### ✅ You MUST:

1. Stop container
2. Remove container
3. Rebuild image
4. Run again

---

## 🧹 Cleanup Commands

### Stop Containers

```bash
docker stop my-server my-client
```

### Remove Containers

```bash
docker rm my-server my-client
```

### Remove Images

```bash
docker rmi my-server-image my-client-image
```

### Remove Network

```bash
docker network rm my-devops-network
```

### ❗ Why Cleanup?

* Avoid conflicts
* Apply new code changes

---

## ✅ Expected Result

* Client connects securely to server
* mTLS handshake succeeds
* Server responds:

```
200 OK
Hello! mTLS Connection Verified.
```

---

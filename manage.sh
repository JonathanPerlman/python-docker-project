#!/bin/bash

cleanup() {
    echo "--- Step 1: Cleaning up old containers and networks ---"
    docker rm -f server-tls client-tls server-mtls client-mtls 2>/dev/null
    docker network rm my-secure-network 2>/dev/null
    docker network create my-secure-network
}

run_tls() {
    cleanup
    echo "--- Step 2: Generating TLS Certificates ---"
    openssl req -x509 -newkey rsa:4096 -keyout ./tls-project/server/server.key -out ./tls-project/server/server.crt -days 365 -nodes -subj "//CN=server-tls"
    cp ./tls-project/server/server.crt ./tls-project/client/

    echo "--- Step 3: Building and Running TLS ---"
    docker build -t server-tls ./tls-project/server
    docker build -t client-tls ./tls-project/client
    
    docker run -d --name server-tls --network my-secure-network server-tls
    sleep 2
    docker run --name client-tls --network my-secure-network client-tls
}

run_mtls() {
    cleanup
    echo "--- Step 2: Generating mTLS Certificates ---"
    # שרת
    openssl req -x509 -newkey rsa:4096 -keyout ./mtls-project/server/server.key -out ./mtls-project/server/server.crt -days 365 -nodes -subj "//CN=server-mtls"
    # לקוח
    openssl req -x509 -newkey rsa:4096 -keyout ./mtls-project/client/client.key -out ./mtls-project/client/client.crt -days 365 -nodes -subj "//CN=my-client"
    
    cp ./mtls-project/server/server.crt ./mtls-project/client/
    cp ./mtls-project/client/client.crt ./mtls-project/server/

    echo "--- Step 3: Building and Running mTLS ---"
    docker build -t server-mtls ./mtls-project/server
    docker build -t client-mtls ./mtls-project/client
    
    docker run -d --name server-mtls --network my-secure-network server-mtls
    sleep 2
    docker run --name client-mtls --network my-secure-network client-mtls
}

case "$1" in
    tls)
        run_tls
        ;;
    mtls)
        run_mtls
        ;;
    *)
        echo "Usage: ./manage.sh [tls|mtls]"
        echo "Example: ./manage.sh mtls"
        ;;
esac

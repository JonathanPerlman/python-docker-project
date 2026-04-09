#!/bin/bash

openssl req -x509 -newkey rsa:4096 -keyout ./server/server.key -out ./server/server.crt -days 365 -nodes -subj "//CN=server-mtls"

openssl req -x509 -newkey rsa:4096 -keyout ./client/client.key -out ./client/client.crt -days 365 -nodes -subj "//CN=my-client"

cp ./server/server.crt ./client/
cp ./client/client.crt ./server/

echo "Certificates generated and exchanged successfully!"
import urllib.request
import time

url = "http://my-server:8000"

print("Client is starting...")

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(f"Log from Server: {body}")
        print(f"Status Code: {response.getcode()}")
except Exception as e:
    print(f"Error: Could not connect to server. {e}")   
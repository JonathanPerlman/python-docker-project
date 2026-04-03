import urllib.request
import ssl

url = "https://my-server:8000"
print("Client is starting (Secure Mode)...")

context = ssl._create_unverified_context()

try:
    with urllib.request.urlopen(url, context=context) as response:
        body = response.read().decode('utf-8')
        print(f"Log from Secure Server: {body}")
        print(f"Status Code: {response.getcode()}")
except Exception as e:
    print(f"Error: Could not connect to SECURE server. {e}")
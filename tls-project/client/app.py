import urllib.request
import ssl

url = "https://server-tls:8000"
print("Client starting in Strict TLS mode...")

context = ssl.create_default_context()
context.load_verify_locations(cafile="server.crt")

try:
    with urllib.request.urlopen(url, context=context) as response:
        print(f"Server Response: {response.read().decode('utf-8')}")
except Exception as e:
    print(f"Security Error: {e}")
     
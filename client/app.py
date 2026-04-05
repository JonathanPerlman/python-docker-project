import urllib.request
import ssl

url = "https://my-server:8000"
print("Client starting in Strict mTLS mode...")

context = ssl.create_default_context()
context.load_verify_locations(cafile="server.crt")
context.load_cert_chain(certfile="client.crt", keyfile="client.key")

try:
    with urllib.request.urlopen(url, context=context) as response:
        print(f"Server Response: {response.read().decode('utf-8')}")
except Exception as e:
    print(f"Security Error: {e}")
     
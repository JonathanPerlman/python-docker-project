import http.server
import ssl
import socketserver
from prometheus_client import start_http_server, Counter

MTLS_PORT = 8000
METRICS_PORT = 9000 

REQUESTS_COUNTER = Counter('mtls_verified_requests_total', 'Total number of verified mTLS requests')

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        REQUESTS_COUNTER.inc()
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello! mTLS Connection Verified.")
        print("Log: Connection verified with Client Certificate!")

httpd = socketserver.TCPServer(("0.0.0.0", MTLS_PORT), MyHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile="client.crt")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    print(f"Metrics available at http://localhost:{METRICS_PORT}")
    
    print(f"Server running on port {MTLS_PORT} with Strict mTLS...")
    httpd.serve_forever()
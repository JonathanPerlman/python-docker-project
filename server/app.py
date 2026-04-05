import http.server
import ssl
import socketserver

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello! mTLS Connection Verified.")
        print("Log: Connection verified with Client Certificate!")

httpd = socketserver.TCPServer(("0.0.0.0", PORT), MyHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile="client.crt")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Server running on port {PORT} with Strict mTLS...")
httpd.serve_forever()
  
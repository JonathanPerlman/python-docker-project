import http.server
import ssl
import socketserver

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello from the SECURE Server! HTTPS is active.")
        print(f"Log: Received a SECURE request!")

httpd = socketserver.TCPServer(("", PORT), MyHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Server is running on HTTPS port {PORT}...")
httpd.serve_forever()

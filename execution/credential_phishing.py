from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# HTTPServer creates a web server, BaseHTTPRequestHandler let you define how requests are handled

host_name = "localhost"
server_port = 8443

#ok so a
class MyServer(BaseHTTPRequestHandler):
    # a special method name recognized by BaseHTTPRequestHandler
    # when GET request arrives, they will handler.do_GET() and "autorun"
    # this is special
    def do_GET(self):
        queries = parse_qs(urlparse(self.path).query)
        #maybe url is like http://localhost:8443/?user=bob&password=123
        print(f"Username: {queries['user'][0]}, Password: {queries['password'][0]}")
        self.send_response(302)
        self.send_header("Location", "http://wwww.google.com")
        self.end_headers()

if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)
    print(f"Server started http://{host_name}:{server_port}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")

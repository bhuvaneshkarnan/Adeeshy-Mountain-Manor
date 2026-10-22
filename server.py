import http.server
import socketserver
import os
import urllib.parse
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Add CORS and caching headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

    def do_GET(self):
        # Clean URLs support: if requesting /en/accommodation, look for /en/accommodation/index.html
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.rstrip('/')
        full_path = os.path.join(DIRECTORY, path.lstrip('/'))

        if os.path.isdir(full_path) and os.path.exists(os.path.join(full_path, 'index.html')):
            if not parsed.path.endswith('/'):
                self.send_response(301)
                self.send_header('Location', parsed.path + '/' + (f'?{parsed.query}' if parsed.query else ''))
                self.end_headers()
                return

        super().do_GET()

def run(port=PORT):
    # Allow address reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('', port), Handler) as httpd:
        print(f'Server running at http://localhost:{port}/')
        print(f'Serving directory: {DIRECTORY}')
        print('Press Ctrl+C to stop.')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nServer stopped.')

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run(port)

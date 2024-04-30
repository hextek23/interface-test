from http.server import HTTPServer, BaseHTTPRequestHandler
import serial
import time

arduino = serial.Serial(port='COM10', baudrate=115200, timeout=.1) 

def writeSerial(x):
    arduino.write(bytes(x, 'utf-8'))

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/on':
            #writeSerial(23)
            self.on_function()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Function triggered')
            return
        elif self.path == '/off':
            self.off_function()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Function triggered')
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def on_function(self):
        # Function to be triggered
        arduino.write(b'23')  # Example: write '1' to Arduino
        
    def off_function(self):
        # Function to be triggered
        arduino.write(b'13')  # Example: write '1' to Arduino

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()

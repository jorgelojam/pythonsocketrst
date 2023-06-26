import http.server
import socketserver
from scapy.all import *

puerto = 8000

class MiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        ruta = self.path
        if ruta == '/':
            mensaje = "Hola desde la página de inicio"
        elif ruta == '/about':
            mensaje = "Esta es la página de acerca de"
        else:
            mensaje = "Página no encontrada"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(mensaje.encode())

        if ruta == '/reset':
            pkt = IP(dst=self.client_address[0])/TCP(dport=self.client_address[1], sport=self.server.server_address[1], flags="R")
            send(pkt, verbose=0)

handler = socketserver.TCPServer(("", puerto), MiHandler)

print(f"Servidor web en funcionamiento en el puerto {puerto}")

handler.serve_forever()
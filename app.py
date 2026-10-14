from http.server import BaseHTTPRequestHandler, HTTPServer


def saludar(nombre="Mundo"):
    return f"Hola {nombre}"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(saludar().encode("utf-8"))


if __name__ == "__main__":
    print("Servidor iniciado en el puerto 5000")
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()

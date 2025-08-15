from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080
path = r'..\html_sample\html\contact.html'


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """
            Метод для обработки входящих GET-запросов
        """
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(path, encoding="utf-8") as file:
            content = file.read()
            self.wfile.write(bytes(content, "utf-8"))  # Тело ответа


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")

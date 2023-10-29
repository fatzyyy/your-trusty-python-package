#!/usr/bin/env python3

import socket
import json


def parse_http_request(request):
    request = request.replace("\n", "\r\n")
    headers, body = request.split("\r\n\r\n", 1)
    headers = headers.split("\r\n")
    method, path, http_version = headers[0].split()
    headers_dict = {h.split(": ")[0]: h.split(": ")[1] for h in headers[1:]}
    return method, path, http_version, headers_dict, body


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 8080)
sock.bind(server_address)
sock.listen(1)

while True:
    print("waiting for connection...")
    connection, client_address = sock.accept()

    try:
        print("connection from", client_address)
        data = connection.recv(1024).decode("utf-8")

        if data:
            method, path, http_version, headers, body = parse_http_request(data)

            if headers["Content-Type"] == "application/json":
                json_data = json.loads(body)
                print("received data:")
                print(json.dumps(json_data, indent=4))

            response = (
                "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>^_^</h1>"
            )
            connection.sendall(response.encode("utf-8"))
        else:
            print("no data from", client_address)
            break

    finally:
        connection.close()

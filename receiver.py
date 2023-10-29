#!/usr/bin/env python3

import socket
import json


def parse_http_request(request):
    parts = request.split("\r\n\r\n", 1)
    if len(parts) == 2:
        headers, body = parts
        headers_lines = headers.split("\r\n")
        content_length = None
        for line in headers_lines:
            if line.lower().startswith("content-length:"):
                content_length = int(line.split(":", 1)[1].strip())
        if content_length is not None:
            if len(body) < content_length:
                raise ValueError("Invalid HTTP Request: Body is not complete")
            body = body[:content_length]
        return headers, body
    else:
        raise ValueError("Invalid HTTP Request: No headers and body separation")


def parse_json_body(body):
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        print("Error: The request body is not a valid JSON")
        return None


def handle_client(client_socket):
    request = b""
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        request += chunk
        if b"\r\n\r\n" in request:
            break
    
    request = request.decode("utf-8")
    print(request)

    try:
        headers, body = parse_http_request(request)
        if not headers.startswith("POST"):
            print("Error: Only POST requests are accepted")
            client_socket.close()
            return
    except ValueError as e:
        print(f"Error: {str(e)}")
        client_socket.close()
        return

    json_data = parse_json_body(body)
    if json_data is not None:
        for key, value in json_data.items():
            print(f"{key}: {value}")

    client_socket.close()


def main():
    port = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"Listening on port {port}...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_socket)


if __name__ == "__main__":
    main()

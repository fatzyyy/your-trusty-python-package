#!/usr/bin/env python3

import socket
import json

def parse_http_request(request):
    headers, body = request.split('\r\n\r\n', 1)
    return headers, body

def parse_json_body(body):
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        print("Error: The request body is not a valid JSON")
        return None

def handle_client(client_socket):
    request = client_socket.recv(4096).decode('utf-8')
    
    headers, body = parse_http_request(request)
    if not headers.startswith('POST'):
        print("Error: Only POST requests are accepted")
        client_socket.close()
        return
    
    json_data = parse_json_body(body)
    if json_data is not None:
        for key, value in json_data.items():
            print(f'{key}: {value}')
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 8080))
    server.listen(5)
    print("Listening on port 8080...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()

import socket

# Server setup
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 65432      # Port to listen on

# socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Allow up to 5 connections

print(f"Listening on {HOST}:{PORT}...")

try:
    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Receiving  logs
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            print(f"Received: {data}")
            # Optionally save the logs to a file
            with open("logs.txt", "a") as file:
                file.write(data + "\n")
        
        client_socket.close()
except KeyboardInterrupt:
    print("Shutting down server.")
finally:
    server_socket.close()

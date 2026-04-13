import socket
import threading

host = "0.0.0.0"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            broadcast(f"{username} left the chat!".encode())
            break

def receive():
    while True:
        client, address = server.accept()
        client.send("USERNAME".encode())
        username = client.recv(1024).decode()

        usernames.append(username)
        clients.append(client)

        broadcast(f"{username} joined the chat!".encode())
        client.send("Connected to server!".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server Running...")
receive()
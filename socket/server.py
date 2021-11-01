import socket
import threading

HOST = '127.0.0.1'
PORT = 25565

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        index = clients.index(client)
        try:
            msg = client.recv(1024)
            msg = msg.decode('utf-8')
            print(f"{nicknames[clients.index(client)]} says {msg}")
            broadcast(f"{nicknames[clients.index(client)]} > {msg}".encode('utf-8'))
        except:
            clients.remove(client)
            client.close()
            nicknames.remove(nicknames[index])
            break

def recieve():
    while True:
        client, addr = server.accept()
        print(f"Connect with {addr}!")

        client.send("NICKNAME".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname.decode('utf-8'))
        clients.append(client)

        print(f"Nickname of client {client} is {nickname}")
        broadcast(f"{nickname.decode('utf-8')} joined the chat!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()





if __name__ == '__main__':
    server.listen()
    print(f"Server running on {HOST}:{PORT}")
    recieve()
import socket

HOST = '127.0.0.1'
PORT = 25565

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

def handle(client):
    valid_command = ['up', 'down', 'right', 'left', 'w', 'a', 's', 'd']
    while True:
        try:
            command = client.recv(1024)
            command = command.decode('utf-8')
            print("Message Recieved from the client!")
            if command in valid_command:
                print(f"We moved {command}!!")
        except:
            break

        

def recieve():
    while True:
        client, addr = server.accept()
        print(f"Connect with {addr}!")

        client.send("Please start pressing key inputs so I can do something with it.....\n".encode('utf-8'))
        handle(client)
    server.close()





if __name__ == '__main__':
    server.listen(1)
    print(f"Server running on {HOST}:{PORT}")
    recieve()
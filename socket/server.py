import socket

HOST = '127.0.0.1'
PORT = 25565

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def run(self):
        self.server.bind((HOST, PORT))
        self.server.listen(5)



if __name__ == '__main__':
    Server().run()
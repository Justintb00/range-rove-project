import socket

HOST = '127.0.0.1'; PORT = 25565

def sendData():
    while True:
        data = str(input("Send the Server something... > "))
        if data == "exit()":
            break
        yield data
def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(bytes('I am sending you some information, server', 'utf-8'))
        data = s.recv(1024)
        yield data.decode('utf-8')
        for msg in sendData():
            msg = bytes(msg, 'utf-8')
            s.send(msg)
            if data:
                print(data.decode('utf-8'))
    s.close()
            
    
            


if __name__ == '__main__':
    for data in client():
        print(data)
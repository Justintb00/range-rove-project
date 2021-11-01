import socket

HOST = '127.0.0.1'; PORT = 25565

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

nickname = None

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                nickname = str(input("Enter a Nickname to Join Chat: "))
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
                msg_out = str(input(f"{nickname} > "))
                client.send(msg_out.encode('utf-8'))

        except ConnectionAbortedError:
            break
    
        except:
            print("Some Error Occured")
            break

    
            
    
            


if __name__ == '__main__':
    client.connect((HOST,PORT))
    recieve()
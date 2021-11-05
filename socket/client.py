import socket
import keyboard

HOST = '192.168.0.225'; PORT = 25565

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

nickname = None

def recieve():
    message = client.recv(1024).decode('utf-8')
    print(message)
    while True:
        try:
            key = keyboard.read_key()
            if key == 'esc':
                break
            print(f"Key {key} sent to the server.....")
            client.send(key.encode('utf-8'))
            

        except ConnectionAbortedError:
            break
    
        except:
            print("Some Error Occured")
            break
    print("Ending the socket connection....")
    client.close()

def readKeys():
    while True:
        key = keyboard.read_key()
        print(key)
            
    
            


if __name__ == '__main__':
    
    client.connect((HOST,PORT))
    recieve()
    
import socket
import select
#from sys import path; path.insert(1, '/home/pi/FreeNove/Code/Server')
#from Motor import Motor

#PWM = Motor()

HOST = '127.0.0.1'
PORT = 25565

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((HOST, PORT))

def handle(client):
    valid_command = ['up', 'w', 'down', 's'] # 'down', 'right', 'left', 'w', 'a', 's', 'd'
    while True:
        try:
            ready = select.select([client], [], [], .2)
            if ready[0]:
                command = client.recv(1024)
                command = command.decode('utf-8')
                print(f"{command}")
                if command in valid_command:
                    print("Message Recieved from the client!")
                    if command == 'w' or command == 'up':
                        #PWM.setMotorModel(-1000,-1000,-1000,-1000)
                        print(f"We moved {command}!!")
                    else:
                        pass
                        #PWM.setMotorModel(1000,1000,1000,1000)
                    #PWM.setMotorModel(0,0,0,0)
            else:
                print("Timeout Bruv")
        except:
            break

        

def recieve():
    while True:
        client, addr = server.accept()
        print(client)
        print(f"Connect with {addr}!")

        client.send("Please start pressing key inputs so I can do something with it.....\n".encode('utf-8'))
        handle(client)
    server.close()

def stop():
    PWM.setMotorModel(0,0,0,0)



if __name__ == '__main__':
    server.listen(1)
    print(f"Server running on {HOST}:{PORT}")
    recieve()
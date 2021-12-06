import websockets
import asyncio

PORT = 8080; HOST='0.0.0.0'

print(f"Server started at {HOST}:{PORT}\nListening......")

clients = []; nicknames = []

directions = ['up', 'down', 'left', 'right', 'w', 'a', 's', 'd']

def broadcast(msg):
    for client in clients:
        client.send("{nickanmes[clients.index(client)]} > {msg}")

async def echo(client, path):
    print("Connection Recieved from Client")
    try:
        while True:
            msg = None
            try:
                msg = await asyncio.wait_for(client.recv(), .2)
            except asyncio.TimeoutError:
                print("Command wasn't recieved")
                continue
            
            if msg in directions:
                print(f"Recieved a direction command --> {msg}")
                await client.send(f"You sent me in the direction {msg}")
                '''
                print("Recieve message from client: " + msg)
                await client.send(f"Res: {'You have successfully sent a message'}")
                print("Sent Message to Client")
                '''

    except websockets.exceptions.ConnectionClosed as e:
        print("The Client Disconnected")
    except KeyboardInterrupt:
        print("Server shutting down.....")

server = websockets.serve(echo, HOST, PORT)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
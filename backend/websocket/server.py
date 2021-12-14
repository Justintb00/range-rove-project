import websockets
import asyncio, json
from urllib import request
from Hand_Detection import handDetector
import numpy as np
from PIL import Image
import io
import cv2


PORT = 8080; HOST='0.0.0.0'

print(f"Server started at {HOST}:{PORT}\nListening......")

clients = []; nicknames = []

directions = ['up', 'down', 'left', 'right', 'w', 'a', 's', 'd', 'stop']

async def echo(client, path):
    print(f"Connection Recieved from Client {client.remote_address}")
    try:
        while True:
            msg = None
            try:
                msg = await asyncio.wait_for(client.recv(), .2)
            except asyncio.TimeoutError:
                #print("Command wasn't recieved")
                continue
            
            msg = json.loads(msg)

            msg_type = msg["message"]; msg = msg["content"]

            if msg_type == "image":
                with request.urlopen(msg) as res:
                    msg = res.read()
            np_img = np.frombuffer(msg, dtype=np.uint8)
            np_img = cv2.imdecode(np_img, flags=cv2.IMREAD_COLOR)
            
            detector = handDetector()
            hand_state = detector.analyze_hand(np_img)
            

            await client.send(f"{hand_state}")
            '''
            if '{' in msg:
                msg = json.loads(msg)["message"]
                if msg == [1,1,1,1,1]:
                    msg = 'up'
                elif msg == [0,0,0,0,0]:
                    msg = 'stop'
                elif msg == [0,1,1,1,1]:
                    msg = 'down'
                elif msg == [0,0,1,1,1]:
                    msg = 'right'
                elif msg == [1,1,0,0,0]:
                    msg = 'left'
                else:
                    await client.send("Nothing to do")
                    continue
            
            if msg == 'stop':
                await client.send('close')

            if msg in directions:
                print(f"Recieved a direction command --> {msg}")
                await client.send(f"You sent me in the direction {msg}")
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
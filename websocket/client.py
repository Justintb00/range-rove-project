import websockets
import asyncio

url = 'ws://127.0.0.1:8080'

async def listen():
    async with websockets.connect(url) as client:
        await client.send("Hi Server!")
        while True:
            msg = await client.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())

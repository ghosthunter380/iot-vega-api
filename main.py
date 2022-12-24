import asyncio
import json
import websockets
    
async def interact(msg):
    async with websockets.connect("ws://192.168.1.109:8002") as websocket:
        await websocket.send(json.dumps(msg))
        odgovor = await websocket.recv()
        return odgovor

def login():
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    msg = {
        "cmd":"auth_req",
        "login":username,
        "password":password
    }
    t = asyncio.run(interact(msg))
    print(json.loads(t))

login()
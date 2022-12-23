import asyncio
import json
import websockets

msg = {
    "cmd":"auth_req",
    "login":"user",
    "password":"user"
    }

async def interact():
    async with websockets.connect("ws://192.168.1.109:8002") as websocket:
        await websocket.send(json.dumps(msg))
        test = await websocket.recv()
        return test
        print(test)
asyncio.run(interact())
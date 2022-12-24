import asyncio
import json
import websockets
import funkcije
    
async def interact(msg):
    async with websockets.connect("ws://192.168.1.109:8002") as websocket:
        await websocket.send(json.dumps(msg))
        odgovor = await websocket.recv()
        return odgovor



funkcije.login()
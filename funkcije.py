import json 
import asyncio
import websockets

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
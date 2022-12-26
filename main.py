import json
import websocket
ws = websocket.WebSocket()
ws.connect("ws://192.168.1.109:8002")

'''ws.send(json.dumps({"cmd":"auth_req", "login":"user", "password":"user"}))
result =  ws.recv()
print (result)'''

def login():
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    msg = {
        "cmd":"auth_req",
        "login":username,
        "password":password
    }
    ws.send(json.dumps(msg))
    print(ws.recv())

def get_payload():
    devEui = input("Please enter devEui: ")
    msg={
        "cmd":"get_data_req",
        "devEui":devEui,
        "select":
        {
            "port":2
        }
    }
    ws.send(json.dumps(msg))
    print(ws.recv())

login()
get_payload()
ws.close()
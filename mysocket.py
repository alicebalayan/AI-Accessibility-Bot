
import websockets
import asyncio
import json



data={"time":-1,"data":""}
async def mysocket(websocket,path):
    global data
    sent=data
    print("started")
    while True:
        data=json.load(open("data"))
        if not float(data["time"]) == float(sent["time"]):
            print(data)
            print(data["data"])
            await websocket.send(data["data"])
            sent=data
        await asyncio.sleep(1)


start_server = websockets.serve(mysocket, host=None,port=8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
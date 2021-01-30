
import websockets
import asyncio



data=""
async def mysocket(websocket,path):
    global data
    sent=data
    print("started")
    while True:
        # name = await websocket.recv()
        # print(f"< {name}")

        # greeting = f"Hello {name}!"

        # await websocket.send(greeting)
        # print(f"> {greeting}")
        data=open("data").read()
        if not data == sent:
            print(data)
            
            sent=data
        await asyncio.sleep(1)


start_server = websockets.serve(mysocket, host=None,port=8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
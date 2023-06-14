import asyncio
import websockets

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            for client in clients:
                await client.send(message)
    finally:
        clients.remove(websocket)

# async def start_server():
#     async with websockets.serve(handler, "localhost", 8000):
#         await asyncio.Future()

# asyncio.run(start_server())

asyncio.get_event_loop().run_until_complete(websockets.serve(handler, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
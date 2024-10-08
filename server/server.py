import os
import asyncio
import websockets

# List to store connected clients
connected_clients = set()
host_name=os.environ.get('HOST_NAME', 'localhost')

async def echo(websocket):
    if websocket not in connected_clients:
        connected_clients.add(websocket)
        print(f"New client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"server: {message}")
            websockets.broadcast(connected_clients, message)
    except websockets.exceptions.ConnectionClosedError:
        # Remove the disconnected client from the list
        connected_clients.remove(websocket)
#        print(f"Client disconnected: {websocket.remote_address}")

async def main():
    async with websockets.serve(echo, host_name, 8765):
#        print("Server started on echo_server:8765")
        await asyncio.Future()  # run forever

asyncio.run(main())

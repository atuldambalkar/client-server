import asyncio
import websockets

async def client():
    """
    Client code to connect to the WebSocket server.
    """
    async with websockets.connect("ws://echo_server:8765") as websocket:
        message = input("Enter a message: ")
        await websocket.send(message)
        while True:
            response = await websocket.recv()
            print(f"Received from server: {response}")

asyncio.get_event_loop().run_until_complete(client())

import os
import asyncio
import websockets

client_id_str=os.environ.get('CLIENT_ID', '1')
client_id=eval(client_id_str)
host_name=os.environ.get('HOST_NAME', 'localhost')
input_dir=os.environ.get('INPUT_DIR', './client')

async def client():
    """
    Client code to connect to the WebSocket server.
    """
    host_url = "ws://" + host_name + ":8765"
    print(host_url)
    async with websockets.connect(host_url) as websocket:
#        message = input("Enter a message: ")
        input_file = input_dir + "/" + "input.txt"
        if os.path.exists(input_file):
            print("File exists")
        else:
            print("File does not exist")
        file = open(input_file, 'r')
        # Get the lines from the file
        lines = file.readlines()
        file.close()
        message = lines[client_id - 1].strip()
        print(message)
        await websocket.send(message)

        outfile_name= input_dir + "/output" + client_id_str + ".json"
        print(outfile_name)
        file = open(outfile_name, "w")
        while True:
            response = await websocket.recv()
            print(f"client: {client_id} {response}")
            file.write(response + "\n")
#            print(f"Received from server: {response}")
            break
        file.close()

asyncio.get_event_loop().run_until_complete(client())

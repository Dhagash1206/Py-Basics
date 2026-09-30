import asyncio
import websockets


async def main():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send("hello from client")
        # Waits for a message broadcast by another client
        print("Received:", await websocket.recv())


asyncio.run(main())

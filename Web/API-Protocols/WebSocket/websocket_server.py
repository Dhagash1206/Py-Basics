# WebSocket: persistent full-duplex connection; server can push anytime.
# Run: python websocket_server.py  (broadcast chat room)
import asyncio
import websockets

connected_clients: set = set()


async def handle_client(websocket):
    connected_clients.add(websocket)
    try:
        async for incoming_message in websocket:
            # Broadcast to everyone except the sender
            await asyncio.gather(
                *(client.send(incoming_message) for client in connected_clients if client is not websocket)
            )
    finally:
        connected_clients.discard(websocket)


async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("WebSocket server on ws://localhost:8765")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())

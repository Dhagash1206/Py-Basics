# Server-Sent Events: one-way server -> client stream over plain HTTP.
# Run: uvicorn sse_server:app --port 8001   |   curl -N localhost:8001/events
import asyncio
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def event_stream():
    while True:
        yield f"data: {datetime.now().isoformat()}\n\n"  # blank line ends an event
        await asyncio.sleep(1)


@app.get("/events")
def events():
    return StreamingResponse(event_stream(), media_type="text/event-stream")

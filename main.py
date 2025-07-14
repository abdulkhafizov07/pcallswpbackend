from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

import database  # noqa

app = FastAPI()

# Allow Next.js frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/vc")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        await websocket.send_text("Welcome to websocket")

        while True:
            data = await websocket.receive_text()
            print("Received:", data)
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        print("Client disconnected")


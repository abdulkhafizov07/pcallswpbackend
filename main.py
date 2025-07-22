from typing import Dict, List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rooms: Dict[str, List[WebSocket]] = {}


@app.websocket("/vc/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    if room_id not in rooms:
        rooms[room_id] = []
    rooms[room_id].append(websocket)

    try:
        while True:
            message = await websocket.receive_json()

            for client in rooms[room_id]:
                if client != websocket:
                    await client.send_json(message)

    except WebSocketDisconnect:
        rooms[room_id].remove(websocket)
        print(f"Client disconnected from room {room_id}")
        if not rooms[room_id]:
            del rooms[room_id]

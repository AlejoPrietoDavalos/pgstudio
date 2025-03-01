import traceback
import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

app = FastAPI()
active_connections = []

class MovementDirection(BaseModel):
    player: int
    x: int
    y: int

# Estado de las pelotas y la última dirección de cada jugador
balls = {
    0: {"x": 400, "y": 300, "speed": 5},
    1: {"x": 400, "y": 300, "speed": 5}
}
directions = {
    0: {"x": 0, "y": 0},
    1: {"x": 0, "y": 0}
}
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            try:
                data = await websocket.receive_json()
                direction = MovementDirection(**data)
                directions[direction.player] = {"x": direction.x, "y": direction.y}
            except WebSocketDisconnect:
                traceback.print_exc()
                active_connections.remove(websocket)
                break

            # Actualizar la posición de cada pelota según la última dirección conocida
            for player, direction in directions.items():
                ball = balls[player]
                ball["x"] += direction["x"] * ball["speed"]
                ball["y"] += direction["y"] * ball["speed"]
                ball["x"] = max(0, min(800, ball["x"]))
                ball["y"] = max(0, min(600, ball["y"]))

            positions = {
                "player_0": {"x": balls[0]["x"], "y": balls[0]["y"]},
                "player_1": {"x": balls[1]["x"], "y": balls[1]["y"]}
            }

            tasks = [asyncio.create_task(connection.send_json(positions)) for connection in active_connections]
            done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

            for task in done:
                try:
                    task.result()
                except WebSocketDisconnect:
                    traceback.print_exc()
                    active_connections.remove(task)

            await asyncio.sleep(1 / 60)

    except WebSocketDisconnect:
        active_connections.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

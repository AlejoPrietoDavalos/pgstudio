import asyncio
import websockets
import json
import time

async def send_receive(websocket):
    last_sent_time = 0
    while True:
        current_time = time.time()
        if current_time - last_sent_time > 1/5:  # Limitar a 5 FPS (5 actualizaciones por segundo)
            # Enviar acciones del jugador
            data = {"x": 1, "y": 1, "action": "move"}
            await websocket.send(json.dumps(data))
            last_sent_time = current_time

        try:
            # Recibir actualizaciones del juego con un timeout para evitar bloquearse
            response = await asyncio.wait_for(websocket.recv(), timeout=1)
            game_state = json.loads(response)
            # Aquí actualizarías el juego con `game_state`
            print("Actualización recibida:", game_state)
        except asyncio.TimeoutError:
            print("Tiempo de espera excedido al recibir datos")
        except websockets.ConnectionClosedOK:
            print("Conexión cerrada de manera limpia")
            break
        except websockets.ConnectionClosedError as e:
            print(f"Error en la conexión: {e}")
            break

async def main():
    async with websockets.connect("ws://localhost:8000/ws") as websocket:
        await send_receive(websocket)

asyncio.run(main())

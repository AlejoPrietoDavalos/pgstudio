import pygame
import sys
import asyncio
import websockets
import json

n_player = int(sys.argv[1])

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego Básico con Pygame")

WHITE = (255, 255, 255)
COLOR_CIRCLE = (255, 0, 0) if n_player == 0 else (0, 0, 255)
COLOR_CIRCLE_OTHER = (0, 0, 255) if n_player == 0 else (255, 0, 0)
ball_radius = 20
clock = pygame.time.Clock()

URI = "ws://localhost:8000/ws"

async def main():
    async with websockets.connect(URI) as websocket:
        direction_last_x, direction_last_y = 0, 0
        # Enviar la dirección inicial (0, 0) para establecer la conexión
        initial_direction = {"player": n_player, "x": 0, "y": 0}
        await websocket.send(json.dumps(initial_direction))
        
        while True:
            print("-")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            direction = {"player": n_player, "x": 0, "y": 0}
            if keys[pygame.K_LEFT]:
                direction["x"] = -1
            if keys[pygame.K_RIGHT]:
                direction["x"] = 1
            if keys[pygame.K_UP]:
                direction["y"] = -1
            if keys[pygame.K_DOWN]:
                direction["y"] = 1

            # Solo enviar la dirección si cambió
            if direction["x"] != direction_last_x or direction["y"] != direction_last_y:
                direction_last_x = direction["x"]
                direction_last_y = direction["y"]
                await websocket.send(json.dumps(direction))

            try:
                positions = await websocket.recv()
                positions = json.loads(positions)
            except websockets.ConnectionClosed:
                print("Connection closed")
                break

            player_ball = positions[f"player_{n_player}"]
            other_ball = positions[f"player_{1 - n_player}"]

            screen.fill(WHITE)
            pygame.draw.circle(screen, COLOR_CIRCLE, (player_ball["x"], player_ball["y"]), ball_radius)
            pygame.draw.circle(screen, COLOR_CIRCLE_OTHER, (other_ball["x"], other_ball["y"]), ball_radius)
            pygame.display.flip()
            clock.tick(20)

if __name__ == "__main__":
    asyncio.run(main())

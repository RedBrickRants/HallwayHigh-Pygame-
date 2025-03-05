import pygame

from entityConfig import Entity
from mapConfig import Room, WALL, FLOOR

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 32
MAP_WIDTH, MAP_HEIGHT = 25, 20
SCREEN_WIDTH, SCREEN_HEIGHT = MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)

# Dungeon Map (0 = Floor, 1 = Wall)
dungeon = [[WALL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

roomtest = Room(20, 12, 5, 5)
roomtest.addWalls()
roomtest.placeInDungeon(dungeon)

#Initialize player
plrPos = roomtest.validSpawn(dungeon)
player = Entity (plrPos, BLUE, 100, 5)

# Pygame Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Roguelike - Basic Map")

def draw_map():
    """Draws the dungeon grid."""
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if dungeon[y][x] == WALL:
                pygame.draw.rect(screen, GRAY, rect)  # Wall
            elif dungeon[y][x] == FLOOR:
                pygame.draw.rect(screen, WHITE, rect)  # Floor
            else:
                pygame.draw.rect(screen, BLACK, rect) #test

def draw_entities():
    #does what it says on the tin
    pygame.draw.rect(screen, player.colour, pygame.Rect(player.x * TILE_SIZE, player.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Game Loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                player.move(0,-1, dungeon)
            elif event.key == pygame.K_DOWN:
                player.move(0,1, dungeon)
            elif event.key == pygame.K_LEFT:
                player.move(-1,0, dungeon)
            elif event.key == pygame.K_RIGHT:
                player.move(1,0, dungeon)

    screen.fill(BLACK)
    
    draw_map()
    draw_entities()
    
    pygame.display.flip()

pygame.quit()

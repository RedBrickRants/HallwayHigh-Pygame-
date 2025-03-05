import random
from typing import Tuple, List

#Tile types
FLOOR = "."
WALL = "#"
PSPAWN = "P"
EXIT = "E"

# Dungeon size
MAP_WIDTH, MAP_HEIGHT = 40, 20

class Room:
	def __init__(self, width:int, height:int, x:int, y:int):
		self.x = x
		self.y = y

		self.width = width
		self.height = height

		#set the floor for the room
		self.layout = [[FLOOR for _ in range(width)]for _ in range(height)]
		self.addWalls()

		print (self.layout)


	def addWalls(self):
		for i in range(self.width):
			self.layout[0][i] = WALL
			self.layout[self.height-1][i] = WALL
		for j in range(self.height):
			self.layout[j][0] = WALL
			self.layout[j][self.width-1]= WALL

	def center(self) -> Tuple[int, int]:
		'''returns the center of the room.'''
		return self.x + self.width//2, self.y + self.height//2

	def overlaps(self, other:'Room')->bool:
		return(
			self.x <other.x +other.width and
			self.x + self.width > other.x and 
			self.y < other.y +other.height and
			self.y + self.height > other.y
		)

	def placeInDungeon(self, dungeon: list[list[str]]):
		for i in range (self.height):
			for j in range(self.width):
				dungeon[self.y + i][self.x + j] = self.layout[i][j]


def create_tunnel(dungeon: List[List[str]], x1: int, y1: int, x2: int, y2: int):
    """Creates a simple L-shaped tunnel between two points."""
    if random.random() < 0.5:
        # Horizontal first, then vertical
        for x in range(min(x1, x2), max(x1, x2) + 1):
            dungeon[y1][x] = FLOOR
        for y in range(min(y1, y2), max(y1, y2) + 1):
            dungeon[y][x2] = FLOOR
    else:
        # Vertical first, then horizontal
        for y in range(min(y1, y2), max(y1, y2) + 1):
            dungeon[y][x1] = FLOOR
        for x in range(min(x1, x2), max(x1, x2) + 1):
            dungeon[y2][x] = FLOOR

def generate_dungeon():
    """Generates a dungeon with rooms and hallways."""
    dungeon = [[WALL for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    rooms = []
    max_rooms = 6  # Adjust as needed

    for _ in range(max_rooms):
        width = random.randint(5, 10)
        height = random.randint(5, 10)
        x = random.randint(1, MAP_WIDTH - width - 1)
        y = random.randint(1, MAP_HEIGHT - height - 1)

        new_room = Room(width, height, x, y)
        if all(not new_room.overlaps(r) for r in rooms):
            new_room.placeInDungeon(dungeon)
            rooms.append(new_room)

    # Connect rooms with hallways
    for i in range(1, len(rooms)):
        x1, y1 = rooms[i - 1].center()
        x2, y2 = rooms[i].center()
        create_tunnel(dungeon, x1, y1, x2, y2)

    # Set player spawn in the first room
    px, py = rooms[0].center()
    dungeon[py][px] = PSPAWN

    # Set exit in the last room
    ex, ey = rooms[-1].center()
    dungeon[ey][ex] = EXIT

    return dungeon

# Generate and print dungeon
dungeon_map = generate_dungeon()
for row in dungeon_map:
    print("".join(row))

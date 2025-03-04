from typing import Tuple

#Tile types
FLOOR = "."
WALL = "#"
PSPAWN = "P"
EXIT = "E"

class Room:
	def __init__(self, width:int, height:int, x:int, y:int):
		self.x = x
		self.y = y

		self.width = width
		self.height = height

		#set the floor for the room
		self.layout = [[FLOOR for _ in range(width)]for _ in range(height)]

	def addWalls(self):
		for i in range(self.width):
			self.layout[0][i] = WALL
			self.layout[self.height-1][i] = WALL
		for j in range(self.height):
			self.layout[j][0] = WALL
			self.layout[j][self.width-1]= WALL

	def overlaps(self, otherRooms)->bool:
		return(
			self.x <otherRooms.x +otherRooms.width and
			self.x + self.width > otherRooms.x and 
			self.y < otherRooms.y +otherRooms.height and
			self.y + self.height > otherRooms.y
		)

	def placeInDungeon(self, dungeon: list[list[str]]):
		for i in range (self.height):
			for j in range(self.width):
				dungeon[self.y + i][self.x + j] = self.layout[i][j]


	def validSpawn(self, dungeon):
		for y in range(self.y, self.y + self.height):
			for x in range(self.x, self.x +self.width):
				if dungeon[y][x] == FLOOR:
					return x,y 
		return 1,1
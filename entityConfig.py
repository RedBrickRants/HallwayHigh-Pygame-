from typing import Tuple


class Entity:
	'''Defines entities''' 
	def __init__(self, x:int, y:int, colour:Tuple[int, int, int], health:int, strength:int, ):

		self.x = x
		self.y = y
		self.colour = colour
		self.health = health
		self.strength = strength

	def move(self, nx:int, ny:int, dungeon):
		newX, newY = self.x + nx, self.y+ny
		print("if youre seeing this it mesans its trying to move")
		if dungeon[newX][newY]== 0:
			self.x =newX
			self.y = newY
			print (f"you moved to ({self.x}{self.y})")
		else:
			print("you cant go there faggot")


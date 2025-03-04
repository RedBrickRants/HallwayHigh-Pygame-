from typing import Tuple

class Entity:
    '''Defines entities''' 
    def __init__(self, pPos:Tuple[int, int], colour:Tuple[int, int, int], health:int, strength:int):
        self.x = pPos[0]
        self.y = pPos[1]
        self.colour = colour
        self.health = health
        self.strength = strength

    def move(self, dx, dy, dungeon):
        # Calculate new positions
        newX, newY = self.x + dx, self.y + dy
        
        print(f"Trying to move to [{newX}, {newY}]")  # Debugging print

        # Ensure the new position is within bounds of the dungeon
        if 0 <= newX < len(dungeon[0]) and 0 <= newY < len(dungeon):
            # Check if it's a walkable space (floor)
            if dungeon[newY][newX] == ".":
                self.x, self.y = newX, newY
                print(f"You moved to [{self.x}, {self.y}]")  # Debugging print
            elif dungeon[newY][newX] == "#":  # Check if it's a wall
                print("That's a wall.")
            else:  # Should never reach here
                print("That's probably the void. How did you get there?")
        else:
            print("You can't move out of bounds!")  # Debugging print

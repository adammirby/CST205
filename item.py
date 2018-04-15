import random

class Item:

  
  # Initializer - requires a name and set x and y to 0
  def __init__(self, name):
    self.name = name
    self.xPos = 0
    self.yPos = 0


  # Based on the map Lonnie created
  def randomLocation(self):
    self.xPos = random.randint(0, 623) / 36 * 36 + 18 
    self.yPos = random.randint(0, 623) / 36 * 36 + 18


  # Set x and y position
  def setPosition(self, x, y):
    self.xPos = x 
    self.yPos = y
    
  # Return x and y position as a list
  def getPosition(self):
    return [self.xPos, self.yPos]

    
# Example of using Item Class    
filename = "/Users/francois/jes/Module7/finalProject/map.jpg"

item = Item('key')
item.randomLocation()

map = makePicture(filename)
addRectFilled(map, item.xPos, item.yPos, 10, 10, yellow)
explore(map)

printNow(item.getPosition())
item.setPosition(18, 18)
printNow(item.getPosition())
addRectFilled(map, item.xPos, item.yPos, 10, 10, yellow)
explore(map)

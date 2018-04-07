import random
#TODO: add inventory local variable
#TODO: add getItem(item) to add to players inventory
#TODO: add hasItem() function to report if player has key
#TODO: add turn variable and modification functions to keep track of number of moves remaining

class Player:
  location = []  #keeps track of current location of player in [x, y]
  lastLocation = [] #keeps track of last location to be used by update to "undraw" last location
  size = None
  
  #initializes plays location to hard coded value
  #DONE: change to random starting locaiton
  #DONE: take map as paramater to see if random starting location is a valid location?
  def __init__(self, map, size):
    locationX = random.randint(0, 499)     #possibly use map functions that return map dimensions?
    locatitonY = random.randomint(0, 499)  #possibly use map functions that return map dimensions?
    while map.validLocation([locationX, locationY]) == False:
      locationX = random.randint(0, 499)
      locatitonY = random.randomint(0, 499)
    self.location.append(locationX)
    self.location.append(locationY)
    self.size = size

  #takes a direction to move the player
  #TODO: determine how far to move player, set distance? let player decide?
  #TODO: needs to check if new location is valid, map class funciton? take map as paramater?
  def movePlayer(self, map, direction):
    self.lastLocation[0] = self.location[0]
    self.lastLocation[1] = self.location[1] 
    if direction == 'r':
      self.location[0] += 20
    elif direction == 'l':
      self.location[0] -= 20
    elif direction == 'u':
      self.location[1] -= 20
    elif direction == 'd':
      self.location[1] += 20
      
  #returns current location of player as a list, index 0 is x, index 1 is y
  def getPlayerLocation(self):
    return self.location
    
  #returns last locaiton of player as a list, index 0 is x, index 1 is y
  #this can be used by the map function to redraw last location back to background color
  def getLastLocation(self):
    return self.lastLocation
      


#FOLLOWING NOT NEEDED, JUST MADE FOR TESTING PLAYER CLASS FUNCTIONS
def makeMap():
  return makeEmptyPicture(500, 500, makeColor(white))
  
def update(map, player):
  loc = player.getLastLocation()
  addRectFilled(map, loc[0], loc[1], 10, 10, makeColor(white))
  loc = player.getPlayerLocation()
  addRectFilled(map, loc[0], loc[1], 10, 10, makeColor(red))
  repaint(map)

def main():
  map = makeMap()
  player = Player()
  while(True):
    update(map, player)
    direction = raw_input("Direction?")
    player.movePlayer(direction)
  
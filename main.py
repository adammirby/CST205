import random


class Map:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.image = makePicture("/Users/francois/cst205/map.jpg")

  def updateMap(self, player, item):
    if not player.hasItem:  # Draw key if player does not have key
      addRectFilled(self.image, item.xPos, item.yPos, 10, 10, yellow)

    loc = player.getLastLocation()
    addRectFilled(self.image, loc[0], loc[1], player.getSize(), player.getSize(), white)

    loc = player.getPlayerLocation()
    if player.hasItem:  # Player is red without key, green with key
      addRectFilled(self.image, loc[0], loc[1], player.getSize(), player.getSize(), green)
    else:
      addRectFilled(self.image, loc[0], loc[1], player.getSize(), player.getSize(), red)

    repaint(self.image)
    
  #Code to get rid of the key after player and key have shared locations
  #Possibly in key class have color attribute (boolean) yellow if player.hasKey
  #is false, white is player.hasKey is true
  
  #def displayKey(location, player.hasItem):
    #Default value for color should be False/yellow
    #This will depend on how item class works
    #Or I can handle it here
    #if(player.hasItem == true):
    
    
  #Funtions that Adam needs
  #getLastLocation() needs to recolor the old player white return a list with 2 indices 0=x, 1=y
  #getPlayerLocation() needs to redraw the player in new location return a list with 2 indices 0=x, 1=y
  
  def returnWidth(self):
    return self.width
  
  def returnHeight(self):
    return self.height
  
  def isValidLocation(self, x, y, size):
    if x + size > self.width or y + size > self.height:
      valid = False
    else:
      valid = True
      
    if valid:
      corners = [[x, y],[x + size + 1, y],[x, y + size + 1],[x + size + 1, y + size + 1]]
      for corner in corners:
        pix = getPixelAt(self.image, corner[0], corner[1])
        if(getColor(pix) == black):
          valid = False
    return valid
  
#TODO: add inventory local variable
#TODO: add getItem(item) to add to players inventory
#TODO: add hasItem() function to report if player has key
#TODO: add turn variable and modification functions to keep track of number of moves remaining


class Player:
  location = [None, None]  #keeps track of current location of player in [x, y]
  lastLocation = [None, None] #keeps track of last location to be used by update to "undraw" last location
  size = None
  hasItem = None

  #initializes plays location to hard coded value
  #DONE: change to random starting locaiton
  #DONE: take map as paramater to see if random starting location is a valid location?
  def __init__(self, map):
    self.size = 10
    locationX = random.randrange(map.returnWidth()) / 36 * 36 + 18    #possibly use map functions that return map dimensions?
    locationY = random.randrange(map.returnHeight()) / 36 * 36 + 18  #possibly use map functions that return map dimensions?

    while map.isValidLocation(locationX, locationY, self.size) == False:
      locationX = random.randrange(map.returnWidth()) / 36 * 36 + 18 
      locationY = random.randrange(map.returnWidth()) / 36 * 36 + 18 

    self.location[0] = locationX 
    self.location[1] = locationY
    self.lastLocation[0] = locationX
    self.lastLocation[1] = locationY
    hasItem = False

  #takes a direction to move the player
  #TODO: determine how far to move player, set distance? let player decide?
  #TODO: needs to check if new location is valid, map class funciton? take map as paramater?
  def movePlayer(self, map, direction, steps):
    self.lastLocation[0] = self.location[0]
    self.lastLocation[1] = self.location[1]

    for i in range (0, steps):
      if direction == 'r' and map.isValidLocation(self.location[0] + 18, self.location[1], self.size):
        self.location[0] += 18
      elif direction == 'l' and map.isValidLocation(self.location[0] - 18, self.location[1], self.size):
        self.location[0] -= 18
      elif direction == 'u' and map.isValidLocation(self.location[0], self.location[1] - 18, self.size):
        self.location[1] -= 18
      elif direction == 'd' and map.isValidLocation(self.location[0], self.location[1] + 18, self.size):
        self.location[1] += 18


  #returns current location of player as a list, index 0 is x, index 1 is y
  def getPlayerLocation(self):
    return self.location

  #returns last locaiton of player as a list, index 0 is x, index 1 is y
  #this can be used by the map function to redraw last location back to background color
  def getLastLocation(self):
    return self.lastLocation

  def getSize(self):
    return self.size

  def pickUpItem(self):
    self.hasItem = True


class Item:
  # Initializer - requires a name and set x and y to 0
  def __init__(self, name):
    self.name = name
    self.xPos = random.randint(0, 623) / 36 * 36 + 18
    self.yPos = random.randint(0, 623) / 36 * 36 + 18

  # Set x and y position
  def setPosition(self, x, y):
    self.xPos = x / 36 * 36 + 18
    self.yPos = y / 36 * 36 + 18

  # Return x and y position as a list
  def getPosition(self):
    return [self.xPos, self.yPos]


def main():
  map = Map(624, 624)
  key = Item('key')
  player = Player(map)
  
  while(True):
    if key.xPos == player.location[0] and key.yPos == player.location[1] and not player.hasItem:
      player.pickUpItem()
      map.updateMap(player, key)
      showInformation("You picked up a key.")
    else:  
      map.updateMap(player, key)
    
    direction = requestString("Direction?")
    direction = direction.split() 
    
    player.movePlayer(map, direction[0], int(direction[1]))
    

main()
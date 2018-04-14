class Map:
  def __init__(self, width, height, image):
    self.width = width
    self.height = height
    self.image = image
  
  def updateMap(self, map, player):
    loc = player.getLastLocation()
    addRectFilled(map, loc[0], loc[1], 10, 10, makeColor(white))
    loc = player.getPlayerLocation()
    addRectFilled(map, loc[0], loc[1], 10, 10, makeColor(red))
    repaint(map)
    
  #Code to get rid of the key after player and key have shared locations
  #Possibly in key class have color attribute (boolean) yellow if player.hasKey
  #is false, white is player.hasKey is true
  
  #def displayKey(location, player.hasItem):
    #Default value for color should be False/yellow
    #This will depend on how item class works
    #Or I can handle it here
    #if(player.hasItem == true):
  
  def returnWidth(self):
    return self.width
  
  def returnHeight(self):
    return self.Height
  
  def isValidLocation(self, x, y):
    pix = getPixelAt(self.image, x, y)
    if(getColor(pix) == black):
      return False
    else:
      return True
    
  ########################################################################################
  #This section contains tools used to draw the first part of the maze for editing.
  #x = 0
  #while x < theMap.width:
    #addRectFilled(mapImage, x, 0, 12, 624)
    #x = x + 36
    
  #y = 0
  #while y < theMap.height:
    #addRectFilled(mapImage, 0, y, 624, 12)
    #y = y + 36
    
  #addRectFilled(mapImage, 300,612, 24, 12, makeColor(139, 69, 19))
  
  #writePictureTo(mapImage, "C://Users//admin//Documents//School//CSUMB//2018//CST205//Module 7//Final Project//mockup.jpg")
  #show(mapImage)
  ########################################################################################
  
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
    locationX = random.randint(0, 623)     #possibly use map functions that return map dimensions?
    locatitonY = random.randomint(0, 623)  #possibly use map functions that return map dimensions?
    while map.validLocation([locationX, locationY]) == False:
      locationX = random.randint(0, 623)
      locatitonY = random.randomint(0, 623)
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

def main():
  map = Map(624, 624, makePicture("C://Users//admin//Documents//School//CSUMB//2018//CST205//Module 7//Final Project//map.jpg"))
  player = Player()
  while(True):
    updateMap(map, player)
    direction = raw_input("Direction?")
    player.movePlayer(direction)
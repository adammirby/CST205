import random


class Map:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.image = makePicture("C://Users//admin//Documents//School//CSUMB//2018//CST205//Module 7//Final Project//map.png")
    self.exitLoc = [306, 612]

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
  
  def isValidLocation(self, x, y, size, hasItem):
    if x + size > self.width or y + size > self.height:
      valid = False
    else:
      valid = True
    if valid:
      corners = [[x, y],[x + size + 1, y],[x, y + size + 1],[x + size + 1, y + size + 1]]
      for corner in corners:
        pix = getPixelAt(self.image, corner[0], corner[1])
        if(getColor(pix) == black or getColor(pix) == makeColor(137,70, 17)):
          valid = False
      if(self.exitLoc[0] == x and self.exitLoc[1] == y and hasItem == False):
        valid = False
      elif(self.exitLoc[0] == x and self.exitLoc[1] == y and hasItem == True):
        valid = True
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
  
  #initializes plays location random starting location
  def __init__(self, map):
    self.size = 10
    self.hasItem = False
    locationX = random.randrange(map.returnWidth()) / 36 * 36 + 18    #possibly use map functions that return map dimensions?
    locationY = random.randrange(map.returnHeight()) / 36 * 36 + 18  #possibly use map functions that return map dimensions?

    while map.isValidLocation(locationX, locationY, self.size, self.hasItem) == False:
      locationX = random.randrange(map.returnWidth()) / 36 * 36 + 18 
      locationY = random.randrange(map.returnWidth()) / 36 * 36 + 18 

    self.location[0] = locationX 
    self.location[1] = locationY
    self.lastLocation[0] = locationX
    self.lastLocation[1] = locationY
    hasItem = False
    
  #takes a direction and number of steps to move
  def movePlayer(self, map, direction, steps):
    self.lastLocation[0] = self.location[0]
    self.lastLocation[1] = self.location[1]

    for i in range (0, steps):
      if direction == 'right' and map.isValidLocation(self.location[0] + 18, self.location[1], self.size, self.hasItem):
        self.location[0] += 18
      elif direction == 'left' and map.isValidLocation(self.location[0] - 18, self.location[1], self.size, self.hasItem):
        self.location[0] -= 18
      elif direction == 'up' and map.isValidLocation(self.location[0], self.location[1] - 18, self.size, self.hasItem):
        self.location[1] -= 18
      elif direction == 'down' and map.isValidLocation(self.location[0], self.location[1] + 18, self.size, self.hasItem):
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
  inputBad = True
  displayIntro()
  playing = True
  
  while(playing):
    if key.xPos == player.location[0] and key.yPos == player.location[1] and not player.hasItem:
      player.pickUpItem()
      map.updateMap(player, key)
      showInformation("You picked up a key.")
    else:  
      map.updateMap(player, key)
      
    while inputBad:
      direction = requestString("                 What direction would you like to move? \n                               Up, Down, Left, or Right \n(Type \'help\' to see the intro again, or \'exit\' to quit the game)") #this is spaced weirdly to try to center text
      direction = direction.lower()
      if direction == 'help':
        displayIntro()
      elif direction == 'exit':
        playing = False
        break
      if direction == "up" or direction == "down" or direction == "left" or direction == "right":
        inputBad = False
    else:
      inputBad = True
      numOfSteps = requestIntegerInRange("Enter the number of steps you would like to move in that direction. \n                   Number can be be in the range of 1-10", 1, 10)  #this is spaced weirdly to try to center text
      player.movePlayer(map, direction, numOfSteps)
      if player.getPlayerLocation() == [306, 612] and player.hasItem:
        playing = False
        break
  map.updateMap(player, key)
  showInformation("You used the key and escaped!")
  showInformation("Thank you for playing!")
  

def displayIntro():
  showInformation("You are trapped in a maze! To get out you will have to find the key and get to the exit!"+
                  " You are the red square, you will be asked for the direction you would like to go (up, down, left, or right),"+ 
                  "and how many steps you would like to take in that direction. You have to grab the yellow key before you can"+
                  " leave through the brown door that leads to freedom! Good Luck!")
                  
def editMap():
  map = makePicture("C://Users//admin//Documents//School//CSUMB//2018//CST205//Module 7//Final Project//map2.jpg")
  addRectFilled(map, 300,612, 24, 12, makeColor(139, 69, 19))
  writePictureTo(map, "C://Users//admin//Documents//School//CSUMB//2018//CST205//Module 7//Final Project//map3.png")
  explore(map)
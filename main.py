from math import sin
import math
class Player():
    
  def __init__(self, _name=None, _points=0.0):
    self.name = _name
    self.points = 0.0 if _points < 0.0 else _points

  #Returns true if player hit the mark or false otherwise 
  def throw(self, _speed, _min, _max):
    r = pow(_speed,2)*sin(math.radians(2*45))/9.8
    if( _min < r < _max):
      return True
    else:
      return False
     
  # set methods
  def setName(self, _name):
    self.name = _name
  def setPoint(self, _points):
    self.points = self.points +  _points

  # get methods
  def getName(self):
    return self.name
  def getPoints(self):
    return self.points


def Game():
  #all the game logic
  return ""


# *TESTING* #
p1 = Player("victor", -10)

print(p1.throw(100,50,100))

print("{0} || {1}".format(p1.getName(), p1.getPoints()))
p1.setName("Ana")
print(p1.getName())
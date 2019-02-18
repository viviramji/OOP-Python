import math 

class Player():
  def __init__(self, _name=None, _points=0.0):
    self.name = _name
    self.points = 0.0 if _points < 0.0 else _points

  #Returns true if player hit the mark or false otherwise 
  def throw(self, _speed, _min, _max):
    r = pow(_speed,2)*math.sin(math.radians(2*45))/9.8
    if( _min < r < _max):
      return True, r
    else:
      return False, r

  # set methods
  def setName(self, _name):
    self.name = _name
  def setPoints(self, _points):
    self.points = self.points +  _points

  # get methods
  def getName(self):
    return self.name
  def getPoints(self):
    return self.points
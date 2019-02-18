from playerModule import Player

def Game():
  n = int(input("How many players: "))
  con, points = 1, [2, 5, 10]
  playerList= []
  while(True):
    player = Player()
    if(con > n): break
    namePlayer = input("Enter {0} player's name -> ".format(con))
    player.setName(namePlayer)
    playerList.append(player)
    con += 1

  
  for i in range(0,2):
    print("Round {0} \n".format(i+1))
    for p in playerList:
      print("{0}'s turn: ".format(p.getName()))
      trying = 1
      while(True):
        if (trying > 3): break
        print("Try number {}".format(trying))
        speed = float(input("Enter start speed: "))
        result, r = p.throw(speed, 200, 220)
        if(result and trying == 1):
          print("Win 10 points")
          p.setPoints(10)
          break
        elif(result and trying == 2):
          print("Win 5 points")
          p.setPoints(5)
          break
        elif( result and trying == 3):
          print("Win 2 points")          
          p.setPoints(2)
          break
        else:
          print("No acertaste pero la distancia maxima fue {0}".format(r))
        trying += 1


Game()
    

# *TESTING* #
""" p1 = playerModule.Player("victor", -10)

print(p1.throw(100,50,100))

print("{0} || {1}".format(p1.getName(), p1.getPoints()))
p1.setName("Ana")
print(p1.getName()) """
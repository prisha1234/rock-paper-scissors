from random import randint
import time 
#creat a list
list = ["rock", "paper ", "scissors"]
#a sign a random play to the computer 
computer = list[randint(0,2)]
#set player to false player not very
player = False 
while player == False:
  #player to true 
  player = input("rock,paper,scissors ?")
  if player == computer:
   print ("tie")
  elif player == "rock":
    if computer == "paper":
      print("computer chooses ",computer)
      time.sleep(2)
      print ("you lose :( ", computer,"covers",player)
    else:
      print("computer chooses ",computer)
      time.sleep(2)
      print ("you win yayyy :D !!!!!!!! ", player ,"breaks",computer)
  elif player == "paper":
    if computer == "rock":
      print("computer chooses ",computer)
      time.sleep(2)
      print("you win yayyy :D !!!!!!!!")
    else:
      print("computer chooses ",computer)
      time.sleep(2)
      print("computer wins yayyy :D !!!!!!!!")
  elif player == "scissors":
    if computer == "rock":
      print("computer chooses ",computer)
      time.sleep(2)
      print("computer win yayyy :D !!!!!!!!")
    else:
      print("computer chooses ",computer)
      time.sleep(2)
      print("you win yayyy :D !!!!!!!!")
  else:
    print("thats not a valid play check ur spellings silly")
  #coding#hacker#classes#player was set to true,but we want it to be false so the loop =continues
    player = False 
 computer = list[randint(0,2)]




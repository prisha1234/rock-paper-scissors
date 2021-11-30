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
  
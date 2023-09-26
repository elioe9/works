print("E P I C    rock, paper, scissors    B A T T L E ")
print("use r, p, s in place of fully written names ")
from getpass import getpass as input
player1 = input("rock, paper or scissors?: ")
player2 = input("rock, paper or scissors?: ")
if player1 == "r" and player2 == "r":
  print("its a tie!!")
elif player1 == "r" and player2 == "p":
    print("p2 paper smothers  p1 rock!")
elif player1 == "r" and player2 == "s" :
    print("p1 rock smashes p2 scissors!")
elif player1 == "p" and player2 == "r" :
  print("p1 paper smothers p2 rock!")
elif player1 == "p" and player2 == "p" :
  print("its a tie!!")
elif player1 == "p" and player2 == "s" :
  print("p2 scissors shreds p1 paper! ")
elif player1 == "s" and player2 == "r" :
  print("p2 rocks smashes p1 scissors!")
elif player1 == "s" and player2 == "p" :
  print("p1 scissors shreds p2 paper!")
elif player1 == "s" and player2 == "s" :
  print(" its a tie!!")
  
elif player2 == "r" and player1 == "r":
  print("its a tie!!")
elif player2 == "r" and player1 == "p":
    print("p1 paper smothers  p2 rock!")
elif player2 == "r" and player1 == "s" :
    print("p2 rock smashes p1 scissors!")
elif player2 == "p" and player1 == "r" :
  print("p2 paper smothers p1 rock!")
elif player2 == "p" and player1 == "p" :
  print("its a tie!!")
elif player2 == "p" and player1 == "s" :
  print("p1 scissors shreds p2 paper! ")
elif player2 == "s" and player1 == "r" :
  print("p1 rocks smashes p2 scissors!")
elif player2 == "s" and player1 == "p" :
  print("p2 scissors shreds p1 paper!")
elif player1 == "s" and player2 == "s" :
  print(" its a tie!!")
else: 
  print("try again!")
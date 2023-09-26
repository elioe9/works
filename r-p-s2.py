print("--- Lets Play ROCK PAPER AND SCISSORS BABY ---")
p1score = 0
p2score = 0
p1 = input("Player1 name? ")
p2 = input("Player2 name? ")
while True:
  
  r = ("R","ROCK","rock","Rock","r")
  s = ("S","s","Scissor","scissor","SCISSOR","s")
  p = ("P","p","Paper","paper","PAPER","p")
  print()
  print ("-Round 1-")
  print()
  print("!Select your moves!")
  p1move = input("Player 1 move>")
  p2move = input("Player 2 move>")

  if p1move in r and p2move in r :
    print(p2 ,"ROCKS AND ROCKS....Its a draw ")
  
  elif p1move in r and p2move in p :
    print(p2,"Wins by wrapping the rock inside it.")
    p2score += 1

  elif p1move in r and p2move in s :
    print(p1,"Wins by breaking the scissors!! ")
    p1score += 1

  elif p1move in p and p2move in r :
    print(p1,"Wins by wrapping Rock ")
    p1score += 1
  
  elif p1move in p and p2move in p :
    print("Its a Draw ")
  
  elif p1move in p and p2move in s :
    print(p2,"Win ")
    p2score += 1
  
  elif p1move in s and p2move in r :
    print(p2,"Wins ")
    p2score += 1

  elif p1move in s and p2move in p :
    print(p1,"Wins ")
    p1score += 1
  else:
    if p1move in s and p2move in s :
      print("Its A draw again  ")
  if p1score == 3 or p2score == 3 :
    print (p1,"has",p1score,"and",p2,"has",p2score)
    break
    
  else:
    continue
    
  
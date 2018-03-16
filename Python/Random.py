from random import randint

while(int(input("Go again?: [1/0]")) != 0):
      x=input("take a guess: ")
      y=randint(1,6)
      if abs(int(x)-int(y)) >= 6 :
          print("too far")
      elif abs(int(x) - int(y)) >0 \
           and abs(int(x) - int(y)) <6 :
              print("not equal")
      else:
          print("Yayyy! Spot on!")

input()

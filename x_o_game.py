#!/usr/bin/python

elements = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
winner = ''

# Show board after each step
def showBoard():
  print(elements[0], elements[1], elements[2])
  print(elements[3], elements[4], elements[5])
  print(elements[6], elements[7], elements[8])

# Return True if we have success combination for 'x' or 'o'
def getSuccessCombinations(el):
  flag = False
  if(checkSuccessCombination("x", el) or checkSuccessCombination("o", el)):
    flag = True
  return flag

# Check if we have success combination on board after each step
def checkSuccessCombination(symbol, el):
  flag = False
  if (el[0] == el[1] == el[2] == symbol or el[3] == el[4] == el[5] == symbol or el[6] == el[7] == el[8] == symbol or
    el[0] == el[3] == el[6] == symbol or el[1] == el[4] == el[7] == symbol or el[2] == el[5] == el[8] == symbol or
    el[0] == el[4] == el[8] == symbol or el[2] == el[4] == el[6] == symbol):
    flag = True
  return flag

# Player turn action
def playerMove(symbol, player):
  step = int(input("%s, your turn. Please enter Your step (numbers range 1-9): " %(player))) - 1
  if(0 <= step < 9):
    while (elements[step] == 'x' or elements[step] == "o"):
      print("Step is already taken")
      step = int(input("%s, your turn. Please enter Your step (numbers range 1-9): " %(player))) - 1
    elements[step] = symbol
    showBoard()
  else:
    print("Wrong symbol")


# Program starts here
player_1 = input("Hi player 1, please enter Your name: ")
player_2 = input("Hi player 2, please enter Your name: ")
showBoard()
getSuccessCombinations(elements)
while not getSuccessCombinations(elements):
  playerMove("x", player_1)
  if (getSuccessCombinations(elements)):
    winner = player_1
    break
  playerMove("o", player_2)
  if (getSuccessCombinations(elements)):
    winner = player_2
    break

print("Success!!!")
print("%s you are winner hahaha!!!" %(winner))
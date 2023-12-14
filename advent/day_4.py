file = open("input/no_4.txt")
test = file.read()
import re
input_2 = test.lower()
container = input_2.split("\n")


#oop approach 

class Game:
  def __init__(winning, hand, function):
    self.winning = winning
    self.hand = hand

p1 = Game(1, 1, sort())



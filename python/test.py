from board import Board
from player import Player
import heuristics

p1 = Player("R")
p2 = Player("G") 
x = Board(p1, p2)

history = []
while x.active:
    move = heuristics.random(x)
    #print x
    #col = int(input("Enter column:"))
    #row = x.find_empty_row(col)
    #move = (col,row)
    x.make_move(move)
    history.append(move)
    if x.check_win(move):
        print(move)
        break

print(x)
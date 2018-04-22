from game import Game
from agent import Agent
import random

game = Game()
starting = random.randint(16,48)
game.fill_random_board(16)

i = 0

''' 
# One player.
while i < 500:
    agent = Agent(game)
    if agent.terminal_test(agent.game):
        break
    card, column = agent.get_action(agent.game)
    game.apply_move(card, column)

    print(game)
    print("Applied move {}, {} in round {}".format(card, column, i+1))

    game.player_move()
    print(game)
    i += 1
'''    

# AI only
while i < 500:
    agent = Agent(game)
    if agent.terminal_test(agent.game):
        break
    card, column = agent.get_action(agent.game)
    game.apply_move(card, column)

    print(game)
    print("Applied move {}, {} in round {}".format(card, column, i+1))
    i += 1   
    




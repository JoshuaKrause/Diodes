from game import Game
from agent import Agent

game = Game()
#game.fill_random_board(32)

i = 0
while i < 200:
    agent = Agent(game)
    if agent.terminal_test(agent.game):
        break
    card, column = agent.get_action(agent.game)
    game.apply_move(card, column)
    total_cards = len(game.active_player.hand) + len(game.other_player.hand) + len(game.board.get_all_cards()) + len(game.deck.discard) + len(game.deck.deck)
    print("Applied move {}, {} in round {}".format(card, column, i))
    print(game)
    print("Active hand: {}    |   Total cards: {}".format(game.other_player.hand, total_cards))
    i += 1
"""
deck_size = len(game.deck.deck)
print(deck_size)
i = 0
while i < deck_size + 50:
    card = game.deck.draw_card()
    print("{}: {}".format(i,card))
    game.deck.discard_card(card)
    i += 1
"""



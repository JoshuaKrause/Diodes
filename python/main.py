from game import Game
from agent import Agent

game = Game()
game.fill_random_board(32)

i = 0
while i < 500:
    agent = Agent(game)
    if agent.terminal_test(agent.game):
        break
    card, column = agent.get_action(agent.game)
    game.apply_move(card, column)

    active_player_hand = len(game.active_player.hand)
    other_player_hand = len(game.other_player.hand)
    active_cards = len(game.board.get_all_cards())
    discard_deck = len(game.deck.discard)
    deck_deck = len(game.deck.deck)
    total_cards =  active_player_hand + other_player_hand + active_cards + discard_deck + deck_deck
    
    print(game)
    print("Applied move {}, {} in round {}".format(card, column, i+1))
    #print("Active hand: {}    |   Total cards: {}".format(game.other_player.hand, total_cards))
    print("Active hand: {} | Other hand: {} | On board: {} | Discard: {} | Deck: {}".format(active_player_hand, other_player_hand, active_cards, discard_deck, deck_deck))
    print("Total: {}".format(total_cards))
    print(game.deck.deck)
    print(game.deck.discard)
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





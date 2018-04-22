import player
import board
import deck
import random
import copy

class Game():

    def __init__(self, player_one=player.Player("ONE"), player_two=player.Player("TWO")):
        self.player_one = player_one
        self.player_two = player_two
        self.active_player = self.player_one
        self.other_player = self.player_two

        self.board = board.Board()
        self.deck = deck.Deck()

        self.player_one.hand = self.deck.draw_hand()
        self.player_two.hand = self.deck.draw_hand()

    def switch_player(self):
        """ Switch current player to the next player. """
        if self.active_player == self.player_one:
            self.active_player = self.player_two
            self.other_player = self.player_one
        else:
            self.active_player = self.player_one
            self.other_player = self.player_two

    def fill_random_board(self, pieces):
        """ Fills the board with random cards.
        pieces = number of desired cards (int)
        """
        total = pieces
        while total > 0:
            column = random.choice(self.board.get_moves())
            card = self.deck.draw_card()
            while card not in deck.COLOR_CARDS:
                self.deck.discard_card(card)
                card = self.deck.draw_card()
            self.board.drop_piece(card, column)
            total -= 1

    def copy_game(self):
        """ Returns a deep copy of the game board.
        Return: Board object
        """
        return copy.deepcopy(self)

    def player_move(self):
        """ Simple game loop function. """
        active = True
        while active:
            player_input = input('Which card,column: ')
            try:
                card, column = player_input.split(',')
                if not self.active_player.check_hand(card):
                    print('Invalid card.')
                    continue
                column = int(column)
                self.apply_move(card, column)
                active = False
            except:
                print('Bad input')
                continue


    def apply_move(self, card, column):
        """ Applies a move to the board and updates the active player's hand. Then switches players.
        card: specified card (string)
        column: target column (int)
        """
        self.active_player.remove_card(card)
        self.active_player.draw_card(self.deck.draw_card())

        score, discards = self.board.play_card(card, column)
        
        self.active_player.score += score
        if discards:
            self.deck.discard_cards(discards)
        
        self.switch_player()

    def forecast_move(self, card, column):
        """ Creates a copy of the game and applies the supplied move.
        card: string
        column: int
        Return: Game object
        """
        game = self.copy_game()
        game.apply_move(card, column)
        return game

    def __str__(self):
        output = str(self.board)
        output += "\n"
        output +="Active player: {}   |   Current hand: {}\n".format(self.active_player.name, self.active_player.show_hand())
        output += "Player One score: {}\nPlayer Two score: {}".format(self.player_one.score, self.player_two.score)
        output += "\n"
        return output



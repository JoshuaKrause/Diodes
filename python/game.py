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

        self.board = board.Board()
        self.deck = deck.Deck()

        self.player_one.hand = self.deck.draw_hand()
        self.player_two.hand = self.deck.draw_hand()

    def switch_player(self):
        """ Switch current player to the next player. """
        if self.active_player == self.player_one:
            self.active_player = self.player_two
        else:
            self.active_player = self.player_one

    def fill_random_board(self, pieces):
        """ Fills the board with random cards.
        pieces = number of desired cards (int)
        """
        total = pieces
        while total > 0:
            x = random.choice(self.board.get_moves())[0]
            card = self.deck.draw_card()
            while card not in deck.COLOR_CARDS:
                self.deck.discard_card(card)
                card = self.deck.draw_card()
            self.board.drop_piece(x, card)
            total -= 1

    def copy_board(self):
        """ Returns a deep copy of the game board.
        Return: board object
        """
        return copy.deepcopy(self.board)

    def loop(self):
        """ Simple game loop function. """
        active = True
        while active:    
            print(self)
            player_input = input('Which card,column: ')
            try:
                card, column = player_input.split(',')
            except:
                print('Bad input')
            if column == 8:
                break
            if not self.active_player.check_hand(card):
                print('Invalid card.')
            else:
                self.active_player.remove_card(card)
                self.active_player.draw_card(self.deck.draw_card())

                score, discards = self.board.play_card(int(column), card)
                
                self.active_player.score += score
                self.deck.discard_cards(discards)
                
                self.switch_player()
            self.loop()

    def __str__(self):
        output = str(self.board)
        output += "\n"
        output +="Active player: {}   |   Current hand: {}\n".format(self.active_player.name, self.active_player.show_hand())
        output += "Player One score: {}\nPlayer Two score: {}".format(self.player_one.score, self.player_two.score)
        output += "\n"
        return output


game = Game()
game.loop()



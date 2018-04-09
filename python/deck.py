from random import shuffle

COLORS = { 
    '0': 'Blank',
    'R': 'Red', # red
    'G': 'Green', # green
    'B': 'Blue', # blue
    'O': 'Yellow', # yellow
    '[': 'Rotate Left', # rotate left
    ']': 'Rotate Right', # rotate right
    '@': 'Flip', # flip
    '!': 'Bomb'  # bomb
    }

COLOR_CARDS = ['R', 'G', 'B', 'O']
SPECIAL_CARDS = ['[', ']', '@', '!']

HAND_SIZE = 3

class Deck():

    def __init__(self, board_size=8):
        """ Creates a deck of colored cards. Total is equal to twice the area of the board.
        board_size: size of the board
        """
        initial_split = 20

        total_cards = board_size ** 2 * 2 # 128 in a default board. 512 in a 16x16 board.
        
        color_multiplier = int(total_cards * .75 / len(COLOR_CARDS))
        special_multiplier = int(total_cards * .25 / len(SPECIAL_CARDS))

        initial_deck = COLOR_CARDS * color_multiplier
        shuffle(initial_deck)

        # The deck is front loaded with 20 color cards.
        self.deck = initial_deck[0:initial_split]

        # Remaining color cards are shuffled with the special cards and added to the back of the deck.
        remaining_deck = initial_deck[initial_split:] + SPECIAL_CARDS * special_multiplier
        shuffle(remaining_deck)
        self.deck = self.deck + remaining_deck
        
        """ The discard begins empty. """
        self.discard = []        

    def shuffle(self):
        """ Refills the deck with discarded cards and shuffles them. """
        self.deck = list(self.discard)
        self.discard = []
        shuffle(self.deck)

    def draw_card(self):
        """ Returns the next card in the deck. If the deck is empty, it shuffles the discards. 
        Return: string
        """
        if len(self.deck) < 1:
            self.shuffle()
        return self.deck.pop(0)

    def draw_hand(self):
        """ Returns a number of cards equal to the required hand size.
        Return: list
        """
        return [self.draw_card() for n in range(HAND_SIZE)]

    def discard_card(self, card):
        """ Puts a card into the discard pile.
        card: string
        """
        self.discard.append(card)

    def discard_cards(self, cards):
        """ Puts multiple cards into the discard pile.
        cards: list (str)
        """
        self.discard += cards

    def get_discard(self):
        """ Returns the current state of the discard pile.
        Return: list (str)
        """
        return self.discard
    
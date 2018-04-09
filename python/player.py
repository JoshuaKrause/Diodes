
class Player():

    def __init__(self, name, AI = None):
        self.name = name
        self.score = 0
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def show_hand(self):
        return ', '.join(self.hand)

    def check_hand(self, card):
        return card in self.hand


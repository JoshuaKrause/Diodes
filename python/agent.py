import random

class Agent():

    def __init__(self, game):
        """ Set up the game for testing and the initial player positions. """
        self.game = game
        self.max_player = self.game.active_player
        self.min_player = self.game.other_player

    def score(self, game):
        """ Compare the final player scores with the original player scores. 
        game: Advanced game (Game object)
        Return: int
        """
        if self.max_player.name == game.active_player.name:
            final_max_player = game.active_player
            final_min_player = game.other_player
        else:
            final_max_player = game.other_player
            final_min_player = game.active_player

        score = (final_max_player.score - self.max_player.score) - (final_min_player.score - self.min_player.score)
        return score

    def get_action(self, game, depth = 3, alpha=float("-inf"), beta=float("inf")):
        """ Returns the best action through minimax searching with alpha-beta pruning.
        game: The initial game object (Game object)
        depth: The maximum depth levels to visit (default 3)
        alpha: The alpha value
        beta: The beta value

        Return: card, column (string, int)
        """
        cards = game.active_player.hand
        moves = game.board.get_moves()

        best_move = (random.choice(cards), random.choice(moves))
        best_score = float("-inf")
        
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        """ 
        for card, column in self.get_all_moves(game):
            score = self.min_value(game.forecast_move(card, column), depth - 1, alpha, beta)
            if score > best_score:
                best_score = score
                best_move = card, column
            alpha = max(best_score, alpha)
        return best_move

    def min_value(self, game, depth, alpha, beta):
        """ Find the minimum value through recusive search.
        game: current game (Game object)
        depth: current depth
        alpha: current alpha value
        beta: current beta value

        Return: int
        """
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()        
        """
        if self.terminal_test(game) or depth == 0:
            return self.score(game)
        else:
            v = float("inf")
            for card, column in self.get_all_moves(game):
                v = min(v, self.max_value(game.forecast_move(card, column), depth - 1, alpha, beta))
                if v <= alpha:
                    return v
                beta = min(v, beta)
            return v

    def max_value(self, game, depth, alpha, beta):
        """ Find the maximum value through recusive search.
        game: current game (Game object)
        depth: current depth
        alpha: current alpha value
        beta: current beta value

        Return: int
        """
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        """
        if self.terminal_test(game) or depth == 0:
            return self.score(game)
        else: 
            v = float("-inf")
            for card, column in self.get_all_moves(game):
                v = max(v, self.min_value(game.forecast_move(card, column), depth - 1, alpha, beta))
                if v >= beta:
                    return v
                alpha = max(v, alpha)
            return v

    def terminal_test(self, game):
        """ Check to see if the board is full. If it is, the game is over.
        Return: boolean
        """
        if not game.board.get_moves():
            return True
        else:
            return False

    def get_all_moves(self, game):
        """ Return all possible moves for the active player.
        game = The current game object

        Return: list
        """
        cards = game.active_player.hand
        moves = game.board.get_moves()
        return list(set([(card, move) for card in cards for move in moves]))

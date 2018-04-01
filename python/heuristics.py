def random(board):
    import random
    moves = board.get_moves()
    return random.choice(moves)
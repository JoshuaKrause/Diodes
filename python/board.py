from deck import COLOR_CARDS, SPECIAL_CARDS

BLANK = '0'
GOAL = 4

class Board():
    """Board class
    Contains all board logic, such as adding pieces, removing pieces, checking for matches.
    """
    
    def __init__(self, size=8):
        """Board initilization

        player_one = the first player (player object)
        player_two = the second player (player object)
        size = the board dimensions (default = 8) (int)

        Creates a board by creating a grid of width by height and filling it with blanks.
        Sets player one as active player.
        """
        self.size = size
        self.state = [[BLANK] * size for row in range(size)]

        self.active = True

    def add_piece(self, card, coordinates):
        """ Adds a piece to the supplied coordinates
        coordinates = the x,y target (tuple)
        piece = the type of piece to place (string)
        """
        try:
            x, y = coordinates
            self.state[y][x] = card
        except:
            print("Invalid coordinates: ", coordinates)

    def remove_piece(self, coordinates):
        """ Clears the supplied coordinates. 
        coordinates = the x,y target (tuple)
        """
        self.add_piece(BLANK, coordinates)

    def get_piece(self, coordinates):
        """ Returns the piece at the coordinates.
        coordinates = the x,y target (tuple)
        Return: string
        """
        x, y = coordinates
        return self.state[y][x]

    def is_blank(self, coordinates):
        """ Checks to see if the specified coordinate is empty.
        coordinates = the x,y target (tuple)
        Return: boolean
        """
        if self.get_piece(coordinates) == BLANK:
            return True
        return False

    def get_all_cards(self):
        """ Returns all the current pieces on the board.
        Return: list (str)
        """
        return [cell for row in self.state for cell in row if cell != BLANK]

    def find_empty_row(self, column):
        """ Find the first empty row in a column.
        column = the x coordinate (int)
        Return: int or None
        """
        for row in range(self.size):
            if self.is_blank((column, row)):
                return row
        return None

    def get_moves(self):
        """ Return the columns that currently have empty rows.
        Return: list (int)
        """
        moves = []
        for column in range(self.size):
            row = self.find_empty_row(column)
            if row == None:
                continue
            if row >= 0:
                moves.append(column)
        return moves

    def drop_piece(self, card, column):
        """ Finds the first empty row of the supplied column and places a piece there.
        column = the x coordiate (int)
        piece = the piece to place (string)
        """
        coordinates = (column, self.find_empty_row(column))
        self.add_piece(card, coordinates)
        return coordinates

    def collapse_board(self):
        """ Collapse the columns so there are no floating cards."""
        columns = [list(row) for row in list(zip(*self.state))]
        collapsed_board = []
        for column in columns:
            collapsed_column = [cell for cell in column if cell != BLANK]
            while len(collapsed_column) < self.size:
                collapsed_column.append(BLANK)
            collapsed_board.append(collapsed_column)
        self.state = [list(row) for row in list(zip(*collapsed_board))]

    def rotate_right(self):
        """ Reconfigure the game state following a clockwise rotation."""
        rotated_state = []
        for col in range(self.size):
            new_row = []
            row = self.size - 1
            while row >= 0:
                new_row.append(self.get_piece((col, row)))
                row -=1
            rotated_state.append(new_row)
        self.state = rotated_state

    def rotate_left(self):
        """ Reconfigure the game state following a counterclockwise rotation."""
        rotated_state = []
        col = self.size - 1
        while col >= 0:
            new_row = []
            for row in range(self.size):
                new_row.append(self.get_piece((col, row)))
            col -= 1
            rotated_state.append(new_row)
        self.state = rotated_state

    def flip(self):
        rotated_state = []
        col = self.size - 1
        while col >= 0:
            new_row = []
            row = self.size - 1
            while row >= 0:
                new_row.append(self.get_piece((row, col)))
                row -= 1
            rotated_state.append(new_row)
            col -= 1
        self.state = rotated_state

    def bomb(self, coordinates):
        """ Explodes along the horizontal, vertical, and diagonal axes. Removes all pieces in targets.
        coordinates = the x,y target (tuple)
        Return: list (str)
        """
        targets = list(set([coord for row in self.find_neighbors(coordinates, limit=self.size) for coord in row]))
        discards = [self.get_piece(cell) for cell in targets if not self.is_blank(cell)]
        for cell in targets:
            self.remove_piece(cell)
        return discards
        

    def find_neighbors(self, coordinates, limit = GOAL):
        """ Returns a list containing the target coordinates' neighbors on the vertical, horizontal, and diagonal axes.
        coordinates = the x,y target (tuple)
        limit = the distance from the origin to return (int)
        Return: list (tuple)
        """
        x,y = coordinates
        x_range = range(x - limit + 1, x + limit)
        y_range = range(y - limit + 1, y + limit)
        scope = range(limit * 2 - 1)

        horizontal = [(x_range[i], y) for i in scope]
        vertical = [(x, y_range[i]) for i in scope]
        down_diagonal = [(x_range[i],y_range[i]) for i in scope]
        up_diagonal = [(x_range[i],y_range[::-1][i]) for i in scope]

        neighbors = []
        for each in [horizontal, vertical, down_diagonal, up_diagonal]:
            filtered_coords = list(filter(lambda x: (x[0] >= 0 and x[1] >= 0) and (x[0] <= self.size - 1 and x[1] <= self.size - 1), each))
            neighbors.append(filtered_coords)

        return neighbors
                  
    def check_match(self, coordinates):
        target = self.get_piece(coordinates)
        total_match = 0
        matches = []

        # If the target is a blank, return the empty list.
        if target == BLANK:
            return matches

        # Iterate through neighbors to see if there are enough matches. 
        neighbors = self.find_neighbors(coordinates)
        for direction in neighbors:
            if len(direction) < GOAL:
                continue
            match = 0
            temp_matches = []
            for cell in direction:
                if self.get_piece(cell) == target:
                    match += 1
                    temp_matches.append(cell)
                else:
                    match = 0
                if match >= GOAL:
                    total_match += 1
                    matches = matches + temp_matches
        return list(set(matches))

    def check_all_match(self):
        """ Iterates through all cells in the board for matches.
        Return: list (tuple)
        """
        matches = []
        for x in range(self.size):
            for y in range(self.size):
                coords = (x, y)
                if not self.is_blank(coords):
                    matches += self.check_match(coords)
        return list(set(matches))

    def clear_matches(self, matches):
        """ Removes matches from the board. Returns cards to discard.
        matches = list (tuple)
        Return: list (str)
        """
        discard = []
        for each in matches:
            discard.append(self.get_piece(each))
            self.remove_piece(each)
        return discard

    def play_card(self, card, column):
        """ Plays a card onto the board. Returns a score and the discarded cards.
        column: int
        card: str
        Return: int, list (str)
        """
        result = self.drop_piece(card, column)
        discards = []
        score = 0
        # If the card played is a color card, check for matches and update the score.
        if card in COLOR_CARDS:
            matches = self.check_match(result)
            if matches:
                score += len(matches)
                discards += self.clear_matches(matches)

        # If the card is a special card, use its unique mechanics.
        else:
            discards.append(self.get_piece(result))
            self.remove_piece(result)
            if card == '[':
                self.rotate_left()
            if card == ']':
                self.rotate_right()
            if card == '@':
                self.flip()
            if card == '!':
                discards += self.bomb(result)
        
        # Collapse the board after each play and check for any secondary matches.
        self.collapse_board()
        matches = self.check_all_match()
        while matches:
            score += len(matches)
            discards += self.clear_matches(matches)
            self.collapse_board()
            matches = self.check_all_match()
        return score, discards

    def __str__(self):
        line_one = "------------------ D I O D E S ------------------\n"
        line_two = "|  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |\n"
        line_thr = "-------------------------------------------------\n\n"
        output = line_one + line_two + line_thr
        rows = self.size - 1
        while rows >= 0:
            output = output + "|  " + "  |  ".join(self.state[rows]) + "  |\n\n"
            rows -= 1
        return output
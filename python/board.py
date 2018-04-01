BLANK = "0"
GOAL = 4

class Board():

    def __init__(self, player_one, player_two, width=8, height=8):
        self.width = width
        self.height = height
        self.state = [[BLANK] * width for row in range(height)]

        self.active = True
        self.player_one = player_one
        self.player_two = player_two

        self.current_player = self.player_one

    def switch_player(self):
        if self.current_player == self.player_one:
            self.current_player = self.player_two
        else:
            self.current_player = self.player_one

    def add_piece(self, coordinates, piece):
        try:
            x, y = coordinates
            self.state[y][x] = piece
        except:
            print("Invalid coordinates: ", coordinates)

    def remove_piece(self, coordinates):
        self.add_piece(coordinates, BLANK)

    def get_piece(self, coordinates):
        x, y = coordinates
        return self.state[y][x]

    def drop_piece(self, column, piece):
        self.add_piece((column, self.find_empty_row(column)), piece)

    def is_blank(self, coordinates):
        if self.get_piece(coordinates) == BLANK:
            return True
        return False

    def find_empty_row(self, column):
        row = 0
        while row < self.height:
            if self.is_blank((column, row)):
                return row
            row += 1
        return None

    def get_moves(self):
        moves = []
        column = 0
        while column <= self.width - 1:
            row = self.find_empty_row(column)
            if row >= 0:
                moves.append((column, row))
            column += 1
        return moves

    def make_move(self, coordinates):
        x,y = coordinates
        color = self.current_player.get_color()
        self.drop_piece(x, color)
        if self.check_win(coordinates):
            print('Win!')
            self.active = False
        else:
            self.switch_player()


    def check_win(self, coordinates):
        target = self.get_piece(coordinates)
        if target == BLANK:
            return False
        for direction in self.find_neighbors(coordinates):
            match = 0
            for cell in direction:
                if self.get_piece(cell) == target:
                    match += 1
                else:
                    match = 0
                if match == GOAL:
                    return True
        return False

    def find_neighbors(self, coordinates):
        x,y = coordinates
        x_range = range(x - GOAL + 1, x + GOAL)
        y_range = range(y - GOAL + 1, y + GOAL)
        scope = range(GOAL * 2 - 1)

        horizontal = [(x_range[i], y) for i in scope]
        vertical = [(x, y_range[i]) for i in scope]
        down_diagonal = [(x_range[i],y_range[i]) for i in scope]
        up_diagonal = [(x_range[i],y_range[::-1][i]) for i in scope]

        neighbors = []
        for each in [horizontal, vertical, down_diagonal, up_diagonal]:
            filtered_coords = list(filter(lambda x: (x[0] >= 0 and x[1] >= 0) and (x[0] <= self.width - 1 and x[1] <= self.height - 1), each))
            if len(filtered_coords) >= GOAL:
                neighbors.append(filtered_coords)

        return neighbors

    def __str__(self):
        output = ""
        rows = self.height - 1
        while rows >= 0:
            output = output + "  ".join(self.state[rows]) + "\n"
            rows -= 1
        return output
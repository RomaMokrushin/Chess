WHITE = 0
BLACK = 1


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


def print_board():
    print('White:')
    for row in range(7, -1, -1):
        for col in range(8):
            if (row, col) in coords:
                if board.field[row][col].char() == 'N':
                    print('N', end='')
                if board.field[row][col].char() == 'B':
                    print('B', end='')
                if board.field[row][col].char() == 'Q':
                    print('Q', end='')
                if board.field[row][col].char() == 'R':
                    print('R', end='')
                if board.field[row][col].char() == 'P':
                    print('P', end='')
                if board.field[row][col].char() == 'K':
                    print('K', end='')
            else:
                print('-', end='')
        print()


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = list()
        for _ in range(8):
            self.field.append([None] * 8)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        pie = self.field[row][col]
        if pie is None:
            return '  '
        color = pie.get_color()
        if color == WHITE:
            cou = 'w'
        else:
            cou = 'b'
        return cou + pie.char()

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in self.field:
            for j in i:
                if j:
                    if j.can_move(row, col) and j.get_color() == color:
                        return True
        return False


class Figure:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color


class Knight(Figure):
    def char(self):
        return 'N'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        if self.row == row or self.col == col:
            return False
        if abs(self.row - row) + abs(self.col - col) != 3:
            return False
        if abs(self.row - row) > 1 or abs(self.row - row):
            return False
        return True


class Bishop(Figure):
    def char(self):
        return 'B'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        if self.row == row or self.col == col:
            return False
        if abs(self.row - row) != abs(self.col - col):
            return False
        return True


class Queen(Figure):
    def char(self):
        return 'Q'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        if (abs(self.row - row) != abs(self.col - col)) and (
                self.row != row and self.col != col):
            return False
        return True


class Rook(Figure):
    def char(self):
        return 'R'

    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True


class Pawn(Figure):
    def char(self):
        return 'P'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        if self.col != col:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if self.row + direction == row:
            return True
        if self.row == start_row and self.row + 2 * direction == row:
            return True
        return False


class King(Figure):
    def char(self):
        return 'K'

    def can_move(self, row, col):
        pass


board = Board()

board.field = [([None] * 8) for i in range(8)]
board.field[0][0] = Rook(0, 0, WHITE)
board.field[0][2] = Knight(0, 2, WHITE)
board.field[0][3] = Bishop(0, 3, WHITE)
board.field[0][3] = Bishop(0, 3, WHITE)
coords = ((0, 0), (0, 2), (0, 3))
print_board()

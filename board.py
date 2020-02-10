from classes.Player import Player


class Board:

    def __init__(self):
        self.ROWS = 6
        self.COLUMNS = 7
        self.clear_board()


    def clear_board(self):
        self._grid = [[None for i in range(self.COLUMNS)] for j in range(self.ROWS)]


    def check_player_wins(self, player):

        id = player.get_id()

        # Check horizontal
        for c in range(self.COLUMNS - 3):
            for r in range(self.ROWS):
                if self._grid[r][c] == id and \
                        self._grid[r][c + 1] == id and \
                        self._grid[r][c + 2] == id and \
                        self._grid[r][c + 3] == id:
                    return True

        # Check vertical
        for c in range(self.COLUMNS):
            for r in range(self.ROWS - 3):
                if self._grid[r][c] == id and \
                        self._grid[r + 1][c] == id and\
                        self._grid[r + 2][c] == id and \
                        self._grid[r + 3][c] == id:
                    return True

        # Check positive diagonal
        for c in range(self.COLUMNS - 3):
            for r in range(self.ROWS - 3):
                if self._grid[r][c] == id and \
                        self._grid[r + 1][c + 1] == id and \
                        self._grid[r + 2][c + 2] == id and \
                        self._grid[r + 3][c + 3] == id:
                    return True

        # Check negative diagonal
        for c in range(self.COLUMNS - 3):
            for r in range(3, self.ROWS):
                if self._grid[r][c] == id and \
                        self._grid[r - 1][c + 1] == id and \
                        self._grid[r - 2][c + 2] == id and \
                        self._grid[r - 3][c + 3] == id:
                    return True

        return False


    def try_add_chip(self, player, column):

        for row in range(self.ROWS):
            if self._grid[row][column] is None:
                self._grid[row][column] = player.get_id()
                return  row

        return -1
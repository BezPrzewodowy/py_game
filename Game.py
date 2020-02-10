import pygame

from classes.Player import Player
from classes.board import Board
from tkinter import *
from tkinter import messagebox

class GameUI:

    def __init__(self, player):
        self.CHIP_OFFSET = 20
        self.BOARD_HEIGHT = 600
        self.SIZE_OF_CHIP = 80
        self.OFFSET = 60
        self.CHIP_RADIUS = int(self.SIZE_OF_CHIP / 2)

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Connect game - PPP')
        Tk().wm_withdraw() #to hide the main window

        self._screen = pygame.display.set_mode((800, 700))
        self._board_img = pygame.image.load("C:/Users/psowa/PycharmProjects/lab1/venv/img/board.png")
        self._board_img_numbers = pygame.image.load('C:/Users/psowa/PycharmProjects/lab1/venv/img/board_numbers.png')
        #self._board_img = pygame.image.load("./img/board.png")
        #self._board_img_numbers = pygame.image.load("./img/board_numbers.png")
        self._font = pygame.font.SysFont('Calibri', 26)

        self.init_ui(player)

    def init_ui(self, player):
        self._screen.fill((255, 255, 255))
        self.draw_board()
        self.draw_player(player)

    def draw_player(self, player):
        pygame.draw.rect(self._screen, (255, 255, 255), [0, 0, 800, 50], 0)
        text = "Current Player: " + player.get_name()
        text = self._font.render(text, True, (0, 0, 0))
        self._screen.blit(text, (50, 10))
        pygame.display.flip()

    def draw_board(self, player=None, row=-1, column=-1):
        if player is not None:
            pygame.draw.circle(self._screen, player.get_color(),
                               (self.OFFSET + self.CHIP_RADIUS + self.CHIP_OFFSET * column + self.SIZE_OF_CHIP * column,
                                self.BOARD_HEIGHT - self.SIZE_OF_CHIP * row - self.CHIP_OFFSET * row), self.CHIP_RADIUS)

        self._screen.blit(self._board_img, (self.OFFSET - 10, self.OFFSET - 10))
        self._screen.blit(self._board_img_numbers,
                          (self.OFFSET + self.CHIP_RADIUS - 10, self.OFFSET + self.BOARD_HEIGHT - 5))

        pygame.display.flip()


class Game:
    def __init__(self):
        self._players = [Player(0), Player(1)]
        self._current_player = 0
        self._board = Board()
        self._gameUI = GameUI(self._players[0])

    def end_game(self,player):
        if messagebox.askquestion(player.get_name() + 'WON!','Restart game?') == 'yes':
                    self.switch_player()
                    self._gameUI.draw_player(self.get_current_player())

    def switch_player(self):
        self._current_player += 1
        self._current_player = self._current_player % 2

    def restart(self):
        self._board.clear_board()
        self._gameUI.init_ui(self.get_current_player())

    def add_chip(self, column):
        player = self.get_current_player()
        return self._board.try_add_chip(player, column)

    def check_player_wins(self, player):
        return self._board.check_player_wins(player)

    def get_board(self):
        return self._board

    def get_player(self, id):
        return self._players[id]

    def get_current_player(self):
        return self._players[self._current_player]

    def game_loop(self):
        row = -1
        column = -1
        valid_keys = [1, 2, 3, 4, 5, 6, 7]
        update_ui = False
        end_game = False
        player_won = False

        while not end_game:
            update_ui = False
            # check for player input events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end_game = True
                elif event.type == pygame.KEYUP:
                        column = (event.key - 49)
                        if column + 1 in valid_keys:
                            row = self.add_chip(column)
                            if row > -1:
                                player_won = self.check_player_wins(self.get_current_player())
                                update_ui = True

            if update_ui:
                self._gameUI.draw_board(self.get_current_player(), row, column)
                if player_won:
                    if messagebox.askquestion(self.get_current_player().get_name() + ' WON!', 'Restart game?')  == 'yes':
                        player_won = False
                        end_game = False
                        self.restart()
                    else:
                        end_game = True
                else:
                    self.switch_player()
                    self._gameUI.draw_player(self.get_current_player())



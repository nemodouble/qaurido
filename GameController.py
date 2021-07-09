from easyAI import TwoPlayersGame
from QuridoBoard import QuridoBoard

class GameController( TwoPlayersGame ):

    def __init__(self, players):
        self.quridoBoard = QuridoBoard()
        self.players = players
        self.nplayer = 1

    def possible_moves(self):
        #print(self.quridoBoard.get_possible_moves(self.nplayer))
        return self.quridoBoard.get_possible_moves(self.nplayer)

    def make_move(self, move):
        if move.find("walk") != -1:
            self.quridoBoard.move_player(self.nplayer, move.split('/')[1])
        elif move.find("jump") != -1:
            self.quridoBoard.jump_player(self.nplayer, move.split('/')[1], move.split('/')[0])
        elif move.find("wall") != -1:
            self.quridoBoard.use_wall(self.nplayer, move.split('/')[1], move.split('/')[2], move.split('/')[3])

    def win(self):
        return self.quridoBoard.is_win(self.nplayer)

    def is_over(self):
        return (self.possible_moves() == []) or self.win()

    def show(self):
        self.quridoBoard.print_board()

    def scoring(self):
        return -self.quridoBoard.calculate_need_turn(self.nplayer)

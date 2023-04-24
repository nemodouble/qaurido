from easyAI import TwoPlayerGame
from QuridoBoard import QuridoBoard

class GameController( TwoPlayerGame ):

    def __init__(self, players):
        self.quridoBoard = QuridoBoard()
        self.players = players
        self.current_player = 1

    def possible_moves(self):
        #print(self.quridoBoard.get_possible_moves(self.nplayer))
        return self.quridoBoard.get_possible_moves(self.current_player)

    def make_move(self, move):
        if move.find("walk") != -1:
            self.quridoBoard.move_player(self.current_player, move.split('/')[1])
        elif move.find("jump") != -1:
            self.quridoBoard.jump_player(self.current_player, move.split('/')[1], move.split('/')[0])
        elif move.find("wall") != -1:
            self.quridoBoard.use_wall(self.current_player, move.split('/')[1], move.split('/')[2], move.split('/')[3])
        elif move == "error":
            None

    def unmake_move(self, move):
        self.quridoBoard.unmake_move(self.current_player, move)

    def is_over(self):
        return self.quridoBoard.calculate_need_turn(self.current_player) == 0

    def show(self):
        self.quridoBoard.print_board()

    def scoring(self):
        score = -self.quridoBoard.calculate_need_turn(self.current_player)
        score += self.quridoBoard.calculate_need_turn(self.nopponent)
        #score += 2*self.quridoBoard.left_wall[self.nplayer]
        return score

from easyAI import TwoPlayersGame

class GameController( TwoPlayersGame ):

    def __init__(self, players):
        self.players = players
        self.board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.possible_move = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.nplayer = 1

    def possible_moves(self):
        return self.possible_move

    def make_move(self, move):
        changed = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.possible_move.remove(move)
        self.board[changed[move-1][0]][changed[move-1][1]] = self.nplayer

    def lose(self):
        for low in (0, 1, 2):
            if self.board[low][0] == self.board[low][1] and self.board[low][1] == self.board[low][2]\
                    and self.board[low][0] == self.nopponent:
                return True
        for clm in (0, 1, 2):
            if self.board[0][clm] == self.board[1][clm] and self.board[1][clm] == self.board[2][clm]\
                    and self.board[0][clm] == self.nopponent:
                return True
        if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] or
            self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]) \
                and self.board[1][1] == self.nopponent:
            return True
        return False

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        print(self.board)

    def scoring(self):
        return -100 if self.lose() else 0 # For the AI

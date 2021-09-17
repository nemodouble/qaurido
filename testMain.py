from QuridoBoard import QuridoBoard
from GameController import GameController
from easyAI import Human_Player, AI_Player, Negamax

testBoard = QuridoBoard()
testBoard.use_wall(1, 6, 10, "horizon")
testBoard.use_wall(1, 6, 8, "vertical")
testBoard.use_wall(1, 8, 6, "horizon")
testBoard.use_wall(1, 12, 6, "horizon")
testBoard.use_wall(1, 16, 6, "horizon")
testBoard.use_wall(1, 2, 10, "horizon")
testBoard.use_wall(2, 2, 10, "horizon")
testBoard.print_board()


# ai = Negamax(4)
# gc = GameController([ Human_Player(), AI_Player(ai) ])
# gc.make_move(1, "walk/up")
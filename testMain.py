from QuridoBoard import QuridoBoard
from GameController import GameController
from easyAI import Human_Player, AI_Player, Negamax

# testBoard = QuridoBoard()
# testBoard.print_board()
# testBoard.move_player(1, "up")
# testBoard.print_board()
# print(testBoard.calculate_need_turn(1))

ai = Negamax(4)
gc = GameController([ Human_Player(), AI_Player(ai) ])
gc.make_move(1, "walk/up")
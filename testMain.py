from QuridoBoard import QuridoBoard
from GameController import GameController
from easyAI import Human_Player, AI_Player, Negamax

testBoard = QuridoBoard()
testBoard.move_player(1, "up")
testBoard.move_player(2, "down")

testBoard.print_board()
print("[아래 : " + str(testBoard.calculate_need_turn(1)) + " / 위 : " + str(testBoard.calculate_need_turn(2)) + "] \n")

testBoard.use_wall(1, 7, 11, "horizon")
testBoard.move_player(2, "left")

testBoard.print_board()
print("[아래 : " + str(testBoard.calculate_need_turn(1)) + " / 위 : " + str(testBoard.calculate_need_turn(2)) + "] \n")

# ai = Negamax(4)
# gc = GameController([ Human_Player(), AI_Player(ai) ])
# gc.make_move(1, "walk/up")
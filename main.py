from GameController import GameController
from easyAI import Human_Player, AI_Player, Negamax
import cProfile

# Start a match (and store the history of moves when it ends)

ai = Negamax(3)
game = GameController( [ AI_Player(ai), AI_Player(ai) ] )
history = game.play()
# cProfile.run("game.play(1)")
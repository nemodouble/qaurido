import GameController
from easyAI import Human_Player, AI_Player, Negamax

# Start a match (and store the history of moves when it ends)

ai = Negamax(6)
game = GameController( [ Human_Player(), AI_Player(ai) ] )
history = game.play()
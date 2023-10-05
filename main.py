from easyAI import Negamax, Human_Player, AI_Player
from jogo_da_velha import JogoDaVelha

ai_depth = 3
ai_algo = Negamax(ai_depth)
JogoDaVelha(Human_Player(), AI_Player(ai_algo)).play()
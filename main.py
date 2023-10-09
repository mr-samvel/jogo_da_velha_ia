from easyAI import Negamax, Human_Player, AI_Player
from jogo_da_velha import JogoDaVelha

player_first = input("Quer ser o X ou O [X | O]?\n>> ") == "X"
heuristic = int(input("Escolha a heuristica de pontuação da IA [0 | 1 | 2]\n 0 - Bloquear oponente\n 1 - Controlar o centro\n 2 - Posicionamento estratégico\n>> "))
ai_depth = 3
ai_algo = Negamax(ai_depth)
JogoDaVelha(Human_Player(), AI_Player(ai_algo), heuristic, player_first).play()
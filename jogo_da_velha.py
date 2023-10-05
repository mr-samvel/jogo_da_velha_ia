from typing import List, Tuple
from easyAI import TwoPlayerGame, Human_Player, AI_Player

class JogoDaVelha(TwoPlayerGame):
    def __init__(self, human: Human_Player, ai: AI_Player):
        self.players = [human, ai]
        self.board = [[self.__empty_symbol for _ in range(3)] for _ in range(3)]
        self.current_player = 1

    @property
    def __empty_symbol(self) -> str:
        return ' '

    @property
    def __symbol(self) -> str:
        return 'X' if self.current_player == 1 else 'O'
    
    @property
    def __opponent_symbol(self) -> str:
        return 'O' if self.current_player == 1 else 'X'

    @property
    def __opponent_won(self) -> bool:
        for row in self.board:
            if all(cell == self.__opponent_symbol for cell in row):
                return True
            
        for col in range(3):
            if all(row[col] == self.__opponent_symbol for row in self.board):
                return True
        
        if all(self.board[i][i] == self.__opponent_symbol for i in range(3)) or\
            all(self.board[i][2-i] == self.__opponent_symbol for i in range(3)):
            return True
        
        return False

    def possible_moves(self) -> List[Tuple[int, int]]:
        return [(row_idx, col_idx)\
                for row_idx, row in enumerate(self.board)\
                for col_idx, value in enumerate(row) if value is self.__empty_symbol]

    def make_move(self, move: Tuple[int, int]) -> None:
        self.board[move[0]][move[1]] = self.__symbol
    
    def unmake_move(self, move: Tuple[int, int]) -> None:
        self.board[move[0]][move[1]] = self.__empty_symbol

    def is_over(self) -> bool:
        return self.__opponent_won or self.possible_moves() is []

    def show(self) -> None:
        print("Possible moves: " + ', '.join(str(e) for e in self.possible_moves()))
        for row in self.board:
            print(row)
        
    def scoring(self):
        return -100 if self.__opponent_won else 0

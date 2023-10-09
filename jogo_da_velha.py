from typing import List, Tuple
from easyAI import TwoPlayerGame, Human_Player, AI_Player

class JogoDaVelha(TwoPlayerGame):
    def __init__(self, human: Human_Player, ai: AI_Player, heuristic: int, player_first: bool):
        self.players = [human, ai] if player_first else [ai, human]
        self.__heuristic = heuristic
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
        print("Jogadas possíveis: " + ', '.join(str(e) for e in self.possible_moves()))
        for row in self.board:
            print(row)
    
    def __heuristic_block_opponent(self) -> int:
        return -100 if self.__opponent_won else 0

    def __heuristic_control_center(self) -> int:
        if self.__opponent_won:
            return -100
        elif self.board[1][1] == self.__symbol:
            return 10
        return 0
    
    def __heuristic_strategic_position(self) -> int:
        if self.__opponent_won:
            return -100
        
        winning_opportunities = 0
        if self.board[1][1] == self.__symbol:
            winning_opportunities += 1
        
        for row in self.board:
            if row.count(self.__symbol) == 2 and row.count(self.__empty_symbol) == 1:
                winning_opportunities += 1
        
        for col in range(3):
            col_symbols = [self.board[row][col] for row in range(3)]
            if col_symbols.count(self.__symbol) == 2 and col_symbols.count(self.__empty_symbol) == 1:
                winning_opportunities += 1
        
        main_diag = [self.board[i][i] for i in range(3)]
        if main_diag.count(self.__symbol) == 2 and main_diag.count(self.__empty_symbol) == 1:
            winning_opportunities += 1
        
        anti_diag = [self.board[i][2 - i] for i in range(3)]
        if anti_diag.count(self.__symbol) == 2 and anti_diag.count(self.__empty_symbol) == 1:
            winning_opportunities += 1

        return winning_opportunities * 5

    def scoring(self) -> int:
        if self.__heuristic == 0:
            return self.__heuristic_block_opponent()
        elif self.__heuristic == 1:
            return self.__heuristic_control_center()
        else:
            return self.__heuristic_strategic_position()

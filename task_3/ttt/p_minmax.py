"""
Author: Katarzyna Nałęcz-Charkiewicz
"""

from board import Board
from player import Player
import numpy


class MinMaxPlayer(Player):
    def __init__(self, name: str, depth_limit: int):
        super().__init__(name)
        self.depth_limit = depth_limit
        self.scores = {
            'x': 1,
            'o': -1,
            "draw": 0
        }
        

    def make_move(self, board: Board, your_side: str):
        move = None
        indexes = self.find_empty_spaces(board)

        best_score = numpy.inf if your_side == 'o' else -numpy.inf
        opponent_side = 'x' if your_side == 'o' else 'o'
        for index in indexes:
            copied_board = board.clone()
            copied_board.board[index] = your_side[:]
            score = self.minimax(copied_board, opponent_side, self.depth_limit)
            
            if your_side == "o":
                if best_score > score:
                    best_score = score
                    move = index
            else:
                if best_score < score:
                    best_score = score
                    move = index
        return move


    def minimax(self, board: Board, side: str, depth: int):
        winner = board.who_is_winner()
        if winner is not None:
            return self.scores[winner]
        indexes = self.find_empty_spaces(board)
        if not indexes:
            return self.scores["draw"]
        
        opponent = 'x' if side == 'o' else 'o'
        best_score = numpy.inf if side == 'o' else -numpy.inf
        for index in indexes:
            copied_board = board.clone()
            copied_board.board[index] = side[:]
            score = self.minimax(copied_board, opponent, depth+1)
            if side == "o":
                best_score = min(best_score, score)
            else:
                best_score = max(best_score, score)
        return best_score

    
    def find_empty_spaces(self, board: Board) -> list[int]:
        return [index for index, character in enumerate(board.board) if character == ' ']

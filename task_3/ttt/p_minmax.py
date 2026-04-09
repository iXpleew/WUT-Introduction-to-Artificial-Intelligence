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
        # TODO
        move = None
        if your_side == 'o':
            best_score = numpy.inf
            indexes = self.find_empty_spaces(board)
            for index in indexes:
                copied_board = board.clone()
                copied_board.board[index] = 'o'[:]
                score = self.minimax(copied_board, 'x', self.depth_limit)
                if best_score > score:
                    best_score = score
                    move = index
        else:
            best_score = -numpy.inf
            for index, spot in enumerate(board.board):
                if spot == " ":
                    copied_board = board.clone()
                    copied_board.board[index] = 'x'[:]
                    score = self.minimax(copied_board, 'o', self.depth_limit)
                    if best_score < score:
                        best_score = score
                        move = index
        return move

        
            

    def minimax(self, board: Board, side: str, depth: int):
        # TODO
        winner = board.who_is_winner()
        if winner is not None:
            return self.scores[winner]
    
        if side == "o":
            best_score = numpy.inf
            for index, character in enumerate(board.board):
                if character == " ":
                    copied_board = board.clone()
                    copied_board.board[index] = side[:]
                    score = self.minimax(copied_board, 'x', depth+1)
                    best_score = min(score, best_score)
            return best_score
        else:
            best_score = -numpy.inf
            for index, character in enumerate(board.board):
                if character == " ":
                    copied_board = board.clone()
                    copied_board.board[index] = side[:]
                    score = self.minimax(copied_board, "o", depth+1)
                    best_score = max(score, best_score)
            return best_score


    def evaluate(self, board: Board, side: str):
        # TODO
        winner = board.who_is_winner()
        if winner is not None:
            return self.scores[winner]
        return None
    
    
    def find_empty_spaces(self, board: Board) -> list[int]:
        empty_spaces = []
        for index, character in enumerate(board.board):
            if character == " ":
                empty_spaces.append(index);
        return empty_spaces

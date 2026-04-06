"""
Author: Katarzyna Nałęcz-Charkiewicz
"""

from board import Board
from player import Player


class MinMaxPlayer(Player):
    def __init__(self, name: str, depth_limit: int):
        super().__init__(name)
        self.depth_limit = depth_limit
        self.scores = {
            'x': 1,
            'o': -1,
            'draw': 0
        }

    def make_move(self, board: Board, your_side: str):
        # TODO
        for index, spot in enumerate(board.board):
            if spot == " ":
                return index
            

    def minimax(self, board: Board, side: str, depth: int):
        # TODO
        if board.who_is_winner() is not None:
            
        return None, None

    def evaluate(self, board: Board, side: str):
        # TODO
        return 0

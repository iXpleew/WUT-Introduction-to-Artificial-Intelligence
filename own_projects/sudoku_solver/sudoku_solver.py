import tkinter as tk

class SudokuSolver:
    def __init__(self) -> None:
        self.position = []
    

    def set_position(self, new_position: list[list[tk.Text]]):
        self.position = new_position

    
    def solve(self):
        self.parse_textfield_values()
        self.check_correctness()

    
    def parse_textfield_values(self):
        parser_position = []
        for index, board in enumerate(self.position):
            parser_position.append([])
            for text_field in board:
                number = text_field.get('1.0', 'end-1c')
                parser_position[index].append(number)
                print(number)
        self.set_position(parser_position)
        
    def check_correctness(self) -> bool:
        # first of all check all of the squares if they are uniqe by set
        for square in self.position:
            if len(set(square)) != square:
                return False
            
        # secondly check horizontally
        for i in range(3):
            for j in range(3):
                return False     
        return True
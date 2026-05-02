import tkinter as tk


def check_correctness(position: list[list[tk.Text]]) -> bool:
    parser_position = []
    for index, board in enumerate(position):
        parser_position.append([])
        for text_field in board:
            number = text_field.get('1.0', 'end-1c')
            print(number)
    return False
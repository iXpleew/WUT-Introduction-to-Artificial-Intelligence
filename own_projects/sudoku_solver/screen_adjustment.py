import tkinter as tk
import sudoku_solver as ssolver


def switch_window_on(root: tk.Tk, solver: ssolver.SudokuSolver):
    root.title("Sudoku solver by iXpleew")
    root.geometry("600x600")

    sudoku_label = tk.Label(root, text="Sudoku solver, enter sample numbers: ")
    sudoku_label.pack()

    button = tk.Button(root, command=solver.solve, text="Calculate!")
    button.pack()
    pass


def get_squares_fields(root: tk.Tk) -> list[list[tk.Text]]:
    current_x = 135
    current_y = 50
    squares = []
    for i in range(9):
        squares.append([])
        if i % 3 == 0 and i > 0:
            current_y += 20
            squares[i-3], squares[i-2], squares[i-1] = set_correct_squares_order(squares[i-3], squares[i-2], squares[i-1])
        for j in range(9):
            if j % 3 == 0:
                current_x += 15
            field = tk.Text(root, height=2, width=2, bg="gray")
            field.place(x=current_x, y=current_y)
            squares[i].append(field)
            current_x += 30
        current_y += 40
        current_x = 135
    return squares


def set_correct_squares_order(first: list[tk.Text], second: list[tk.Text], third: list[tk.Text]):
    new_first = first[:3] + second[:3] + third[:3]
    new_second = first[3:6] + second[3:6] + third[3:6]
    new_third = first[6:] + second[6:] + third[6:]
    return new_first, new_second, new_third


def main_window():
    root = tk.Tk()
    sudoku_solver = ssolver.SudokuSolver()

    switch_window_on(root, sudoku_solver)
    sudoku_solver.set_position(get_squares_fields(root))
    
    root.mainloop()
 
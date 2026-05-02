import tkinter as tk
import sudoku_solver as ssolver


def switch_window_on(root: tk.Tk, solver: ssolver.SudokuSolver):
    root.title("Sudoku solver by iXpleew")
    root.geometry("600x600")

    sudoku_label = tk.Label(root, text="Sudoku solver, enter sample numbers: ")
    sudoku_label.pack()

    button = tk.Button(root, command=solver.solve, text="Calculate!")
    pass


def get_squares_fields(root: tk.Tk) -> list[list[tk.Text]]:
    current_x = 135
    current_y = 40
    squares = []
    for i in range(9):
        squares.append([])
        if i % 3 == 0:
            current_y += 20
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


def main_window():
    root = tk.Tk()
    sudoku_solver = ssolver.SudokuSolver()

    switch_window_on(root, sudoku_solver)
    position = get_squares_fields(root)
    root.mainloop()
 
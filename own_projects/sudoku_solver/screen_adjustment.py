import tkinter as tk

def switch_window_on():
    root = tk.Tk()
    root.title("Sudoku solver by iXpleew")
    root.geometry("400x400")

    sudoku_label = tk.Label(root, text="Sudoku solver, enter sample numbers: ")
    sudoku_label.pack()
    root.mainloop()
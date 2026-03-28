import tkinter as tk

def switch_window_on():
    root = tk.Tk()
    root.title("Sudoku solver by iXpleew")
    root.geometry("600x600")

    sudoku_label = tk.Label(root, text="Sudoku solver, enter sample numbers: ")
    sudoku_label.pack()

    current_x = 135
    current_y = 40
    for i in range(9):
        if i % 3 == 0:
            current_y += 20
        for j in range(9):
            if j % 3 == 0:
                current_x += 15
            field = tk.Text(root, height=2, width=2, bg="gray")
            field.place(x=current_x, y=current_y)
            current_x += 30
        current_y += 40
        current_x = 135
    root.mainloop()

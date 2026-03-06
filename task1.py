import matplotlib.pyplot as plt
import numpy as np


def visualize_fun(obj_fun: callable, trajectory: np.ndarray):
    min_x, min_y = trajectory[-1]
    MIN_X = 10
    MAX_X = 10
    PLOT_STEP = 100

    x1 = np.linspace(-MIN_X, MAX_X, PLOT_STEP)
    x2 = np.linspace(-MIN_X, MAX_X, PLOT_STEP)
    X1, X2 = np.meshgrid(x1, x2)
    Z = obj_fun(X1, X2)

    plt.figure(figsize=(8, 6))
    plt.pcolormesh(X1, X2, Z, cmap='viridis', shading='auto')
    plt.colorbar(label='Objective Function Value')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Objective Function Visualization')

    plt.scatter(min_x, min_y, color='yellow', label='Minimum found by gradient descent alg.')
    plt.plot(trajectory[:, 0], trajectory[:, 1], marker='o', color='red', label='Gradient Descent Steps', alpha=0.5)

    plt.legend()
    plt.show()

# 1. Definiujemy funkcję celu (np. miska/paraboloida)
# f(x1, x2) = x1^2 + x2^2
def my_bowl_function(x1, x2):
    return x1**2 + x2**2

# 2. Tworzymy sztuczną trajektorię "schodzenia" do minimum
# Algorytm startuje w (8, 8) i idzie w stronę (0, 0)
fake_trajectory = np.array([
    [8.0, 8.0],
    [6.0, 6.0],
    [4.0, 3.5],
    [2.0, 2.0],
    [1.0, 0.5],
    [0.1, 0.1]  # To zostanie uznane za znalezione minimum (ostatni element)
])

# 3. Wywołanie Twojej funkcji
visualize_fun(my_bowl_function, fake_trajectory)
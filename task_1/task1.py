import matplotlib.pyplot as plt
import autograd.numpy as anp
import numpy as np
import autograd
from typing import Callable
import math
import random

def paraboloid(args: list[float]) -> float:
    x1, x2 = args[0], args[1]
    return x1**2 + x2**2


def matyas(args: list[float]) -> float:
    x1, x2 = args[0], args[1]
    return 0.26 * (x1**2 + x2**2) - 0.48 * x1 * x2


def get_random_point():
    return [random.randrange(-20, 20)/2, random.randrange(-20,20)/2]


def gradient_descent_formula(argument: float, learning_rate: float, vector_arg: float) -> float:
    new_xt = argument - learning_rate*vector_arg
    return new_xt


def calculate_gradient_path(function: Callable, xt=None, learning_rate=0.07):
    if xt is None:
        xt = [0.0, 0.0]
    function_gradient = autograd.grad(function)
    gradient_history = [[xt[0], xt[1]]]
    for i in range(999):
        vector_gradient = function_gradient(anp.array(xt))
        xt[0] = gradient_descent_formula(xt[0], learning_rate, vector_gradient[0])
        xt[1] = gradient_descent_formula(xt[1], learning_rate, vector_gradient[1])
        gradient_history.append([xt[0], xt[1]])

        low_gradient = math.sqrt(vector_gradient[0]**2 + vector_gradient[1]**2) < 0.01
        if low_gradient: 
            break
    return np.array(gradient_history)


def calculate_vector_values(trajectory: np.ndarray, function: Callable) -> list[float]:
    values = []
    for coordinates in trajectory:
        values.append(function(coordinates))
    return values


def visualize_fun(obj_fun: Callable, trajectories: list[np.ndarray]): 
    min_x1, min_y1 = trajectories[0][-1]
    min_x2, min_y2 = trajectories[1][-1]
    min_x3, min_y3 = trajectories[2][-1]
    MIN_X = 10
    MAX_X = 10
    PLOT_STEP = 100

    x1 = np.linspace(-MIN_X, MAX_X, PLOT_STEP)
    x2 = np.linspace(-MIN_X, MAX_X, PLOT_STEP)
    X1, X2 = np.meshgrid(x1, x2)
    Z = obj_fun([X1, X2])

    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12, 6)) 

    plt.subplots_adjust(bottom=0.25)
    map = ax1.pcolormesh(X1, X2, Z, cmap='viridis', shading='auto')
    fig.colorbar(map, ax=ax1, label='Objective Function Value')
    ax1.set_xlabel('x1')
    ax1.set_ylabel('x2')
    ax1.set_title('Objective Function Visualization')

    def set_scatters(min, max, trajectory, colour):
        ax1.scatter(min, max, color="yellow")
        ax1.plot(trajectory[:, 0], trajectory[:, 1], marker='o', color=colour, alpha = 0.5)

    set_scatters(min_x1, min_y1, trajectories[0], "lime")
    set_scatters(min_x2, min_y2, trajectories[1], "magenta")
    set_scatters(min_x3, min_y3, trajectories[2],"tomato")

    a_values = calculate_vector_values(trajectories[0], obj_fun)
    b_values = calculate_vector_values(trajectories[1], obj_fun)
    c_values = calculate_vector_values(trajectories[2], obj_fun)
    ax2.plot(range(len(a_values)), a_values, color="lime", label=f"{trajectories[0][0]}")
    ax2.plot(range(len(b_values)), b_values, color="magenta", label=f"{trajectories[1][0]}")
    ax2.plot(range(len(c_values)), c_values, color="tomato", label=f"{trajectories[2][0]}")
    ax2.set_xlabel("Number of iteration")
    ax2.set_ylabel("Value")
    ax2.legend(title="Starting points")
    plt.show()

if __name__== "__main__":
    first_traj = calculate_gradient_path(paraboloid, get_random_point())
    second_traj = calculate_gradient_path(paraboloid, get_random_point())
    third_traj = calculate_gradient_path(paraboloid, get_random_point())
    visualize_fun(paraboloid, [first_traj, second_traj, third_traj])
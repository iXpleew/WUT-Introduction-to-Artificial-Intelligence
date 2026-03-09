import matplotlib.pyplot as plt
import autograd.numpy as anp
import numpy as np
import autograd
from typing import Callable
import math
# co zmienic:
# - usunac suwak
# - dodac argparse
# - dodac druga funkcje
# - parametry skoku, liczbe iteracji
# - wykres skoku i wniosek w pdf jaki ma wplyw na algorytm
# - wykres punktow i jak sie zmianiaja 
 

def paraboloid(args: list[float]) -> float:
    x1, x2 = args[0], args[1]
    return x1**2 + x2**2

def matyas(args: list[float]) -> float:
    x1, x2 = args[0], args[1]
    return 0.0

def gradient_descent_formula(argument: float, learning_rate: float, vector_arg: float) -> float:
    new_xt = argument - learning_rate*vector_arg
    return new_xt

def calculate_gradient_path(function: Callable, learning_rate: float, iteration_number: int, xt=None): 
    if xt is None:
        xt = [0.0, 0.0]
    function_gradient = autograd.grad(function) # type: ignore
    gradient_history = [[xt[0], xt[1]]]
    for i in range(iteration_number):
        vector_gradient = function_gradient(anp.array(xt))
        xt[0] = gradient_descent_formula(xt[0], learning_rate, vector_gradient[0])
        xt[1] = gradient_descent_formula(xt[1], learning_rate, vector_gradient[1])
        gradient_history.append([xt[0], xt[1]])

        low_gradient = math.sqrt(vector_gradient[0]**2 + vector_gradient[1]**2) < 0.001
        if i >= 999 or low_gradient: 
            break
    return np.array(gradient_history)

def check_rate_influance(xt: list[float]):
    pass    

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

    def set_scatters(min, max, trajectory):
        ax1.scatter(min, max, color="yellow")
        ax1.plot(trajectory[:, 0], trajectory[:, 1], marker='o', color='red', alpha = 0.5)

    set_scatters(min_x1, min_y1, trajectories[0])
    set_scatters(min_x2, min_y2, trajectories[1])
    set_scatters(min_x3, min_y3, trajectories[2])
    values = []
    for vector in trajectories[2]:
        values.append(paraboloid(vector))

    ax2.plot(range(len(trajectories[2])), values)  
    
    ax1.legend()
    plt.show()

first_traj = calculate_gradient_path(paraboloid, 0.9, 2, [1., 1.])
second_traj = calculate_gradient_path(paraboloid, 0.2, 100, [10., -4.])
third_traj = calculate_gradient_path(paraboloid, 0.01, 2000, [6., -7.])
visualize_fun(paraboloid, [first_traj, second_traj, third_traj])
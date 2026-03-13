import matplotlib.pyplot as plt
import autograd.numpy as anp
import numpy as np
import autograd
from typing import Callable
import math
import random
# co zmienic:
# - parametry skoku, liczbe iteracji
# - wykres skoku i wniosek w pdf jaki ma wplyw na algorytm
# - wykres punktow i jak sie zmianiaja 
# - zmienic calculate gradient path zeby zwracal liste list tego jak sie zmienia gradient
# zeby wyswietlacv potem pokazywac na jednym wykresie 
 

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

def calculate_gradient_path(function: Callable, iteration_number: int, xt=None):
    learning_rate = 0.1
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

def calculate_vector_values(trajectory: np.ndarray) -> list[float]:
    values = []
    for coordinates in trajectory:
        values.append(paraboloid(coordinates))
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

    layout = (("heatmap", "point_a"),
              ("heatmap", "point_b"),
              ("heatmap", "point_c"))
    
    fig, axes = plt.subplot_mosaic(layout, figsize=(12, 6),constrained_layout=True) #type: ignore

    plt.subplots_adjust(bottom=0.25)
    map = axes["heatmap"].pcolormesh(X1, X2, Z, cmap='viridis', shading='auto')
    fig.colorbar(map, ax=axes["heatmap"], label='Objective Function Value')
    axes["heatmap"].set_xlabel('x1')
    axes["heatmap"].set_ylabel('x2')
    axes["heatmap"].set_title('Objective Function Visualization')

    def set_scatters(min, max, trajectory):
        axes["heatmap"].scatter(min, max, color="yellow")
        axes["heatmap"].plot(trajectory[:, 0], trajectory[:, 1], marker='o', color='red', alpha = 0.5)

    set_scatters(min_x1, min_y1, trajectories[0])
    set_scatters(min_x2, min_y2, trajectories[1])
    set_scatters(min_x3, min_y3, trajectories[2])

    a_values = calculate_vector_values(trajectories[0])
    b_values = calculate_vector_values(trajectories[1])
    c_values = calculate_vector_values(trajectories[2])
    axes["point_a"].plot(range(len(a_values)), a_values)
    axes["point_a"].set_xlabel("First point")
    axes["point_b"].plot(range(len(b_values)), b_values)
    axes["point_b"].set_xlabel("Second point")
    axes["point_c"].plot(range(len(c_values)), c_values)
    axes["point_c"].set_xlabel("Third point")

    axes["heatmap"].legend()
    plt.show()

first_traj = calculate_gradient_path(paraboloid, 20, [get_random_point()])
second_traj = calculate_gradient_path(paraboloid, 10, [get_random_point()])
third_traj = calculate_gradient_path(paraboloid, 20, [get_random_point()])
visualize_fun(paraboloid, [first_traj, second_traj, third_traj])
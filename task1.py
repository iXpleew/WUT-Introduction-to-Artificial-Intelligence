import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import autograd.numpy as anp
import numpy as np
import autograd
 

def paraboloid(args: list[float]) -> float:
    x1, x2 = args[0], args[1]
    return x1**2 + x2**2

def gradient_descent_formula(argument: float, learning_rate: float, vector_arg: float) -> float:
    new_xt = argument - learning_rate*vector_arg
    return new_xt

def calculate_gradient_path(function: callable, xt: list[float], learning_rate: float, iteration_number: int): 
    function_gradient = autograd.grad(function)
    gradient_history = [[xt[0], xt[1]]]
    for i in range(iteration_number):
        vector_gradient = function_gradient(anp.array(xt))
        xt[0] = gradient_descent_formula(xt[0], learning_rate, vector_gradient[0])
        xt[1] = gradient_descent_formula(xt[1], learning_rate, vector_gradient[1])
        gradient_history.append([xt[0], xt[1]])
        if i >= 999: 
            break
    return np.array(gradient_history)
        

def visualize_fun(obj_fun: callable, trajectory: np.ndarray, rate: float, iteration: int): #type: ignore
    min_x, min_y = trajectory[-1]
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

    x1_ax_slider = fig.add_axes([0.127, 0.05, 0.28, 0.03])
    x2_ax_slider = fig.add_axes([0.05, 0.25, 0.03, 0.65])

    x1_slider = Slider(ax=x1_ax_slider, label="x1", valmin=-10.0, valmax=10.0, valinit=0, orientation='horizontal')
    x2_slider = Slider(ax=x2_ax_slider, label="x2", valmin=-10.0, valmax=10.0, valinit=0, orientation="vertical")

    ax1.scatter(min_x, min_y, color='yellow', label='Minimum found by gradient descent alg.')
    ax1.plot(trajectory[:, 0], trajectory[:, 1], marker='o', color='red', label='Gradient Descent Steps', alpha=0.5)

    def update_plot(val):
        new_points = [x1_slider.val, x2_slider.val]
        trajectory = calculate_gradient_path(obj_fun, new_points, rate, iteration)
        fig.canvas.draw_idle()
        min_x, min_y = trajectory[-1]
        ax1.scatter(min_x, min_y, color='yellow', label='Minimum found by gradient descent alg.')
        ax1.plot(trajectory[:, 0], trajectory[:, 1], marker='o', color='red', label='Gradient Descent Steps', alpha=0.5)

    x1_slider.on_changed(update_plot)
    x2_slider.on_changed(update_plot)

    ax1.legend()
    plt.show()


trajectory = calculate_gradient_path(paraboloid, learning_rate=.1, xt=[0., 0.], iteration_number=100)
visualize_fun(paraboloid, trajectory, rate=0.1, iteration = 100)
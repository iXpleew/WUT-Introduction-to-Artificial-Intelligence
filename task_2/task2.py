from matplotlib import pyplot as plt
import random
import math 

def generate_random_points(number_of_points: int) -> list[list[int]]:
    points_list = []
    for i in range(number_of_points):
        points_list.append([random.randrange(-20, 20), random.randrange(-20,20)])
    return points_list


def calculate_distance(point_a: list[int], point_b: list[int]) -> float:
    distance = math.sqrt((point_b[0]-point_a[0])**2 + (point_b[1]-point_a[1])**2)
    return distance


def calculate_total_distance(points:list[list[int]]) -> float:
    total_distance = 0
    for i in range(len(points)):
        first_point = points[i-1]
        second_point = points[i]
        total_distance += calculate_distance(first_point, second_point)
    return total_distance


def shuffle_list(points:list[list[int]], shuffle_number: int) -> list[list[list[int]]]:
    combination_list = []
    starting_point = points[0]
    rest_points = points[1:]
    for _ in range(shuffle_number):
        random.shuffle(rest_points)
        combination = [starting_point] + rest_points
        combination_list.append(combination)
    return combination_list


def genetic_selection(shuffled_lists: list[list[list[int]]]) -> list[list[list[int]]]:
    random.shuffle(shuffled_lists)
    mid_number = len(shuffled_lists) // 2
    survivors = []
    for i in range(mid_number):
        first_lenght = calculate_total_distance(shuffled_lists[i])
        second_lenght = calculate_total_distance(shuffled_lists[i + mid_number])
        if first_lenght > second_lenght:
            survivors.append(shuffled_lists[i])
        else:
            survivors.append(shuffled_lists[i + mid_number])
    return survivors


def show_points_on_plane(points:list[list[int]], generation_number: int):
    x_coordinates = [x[0] for x in points]
    y_coordinates = [x[1] for x in points]
    distance = calculate_entire_distance(points)
    x_coordinates.append(x_coordinates[0])
    y_coordinates.append(y_coordinates[0])
    plt.scatter(x_coordinates, y_coordinates)
    plt.plot(x_coordinates, y_coordinates)
    plt.legend([f"Total distance: {distance:.2f}", f"Generation: {generation_number}"])
    plt.show()

if __name__ == "__main__":
    list_points = [[-14, 8], [-4, 17], [13, -10], [-11, -12], [-4, 13], [-20, -12], [-4, 9], [-12, 18], [-4, -2], [-16, 11]]
    show_points_on_plane(list_points, 1)
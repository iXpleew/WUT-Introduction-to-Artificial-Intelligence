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


def shuffle_list(points:list[list[int]], shuffle_number: int) -> list[list[list[int]]]:
    combination_list = []
    for i in range(shuffle_number):
        combination_list.append(random.shuffle(points))
    return combination_list


def show_points_on_plane(points:list[list[int]]):
    
    random.shuffle(points)
    x_coordinates = [x[0] for x in points]
    y_coordinates = [x[1] for x in points]

    # for connecting all points
    x_coordinates.append(x_coordinates[0])
    y_coordinates.append(y_coordinates[0])
    plt.scatter(x_coordinates, y_coordinates)
    plt.plot(x_coordinates, y_coordinates)
    plt.show()

if __name__ == "__main__":
    list_points = [[-14, 8], [-4, 17], [13, -10], [-11, -12], [-4, 13], [-20, -12], [-4, 9], [-12, 18], [-4, -2], [-16, 11]]
    show_points_on_plane(list_points)
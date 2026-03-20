from matplotlib import pyplot as plt
import random 

def generate_random_points(number_of_points: int) -> list[list[int]]:
    points_list = []
    for i in range(number_of_points):
        points_list.append([random.randrange(-20, 20), random.randrange(-20,20)])
    return points_list


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

list_points = [[-14, 8], [-4, 17], [13, -10], [-11, -12], [-4, 13], [-20, -12], [-4, 9], [-12, 18], [-4, -2], [-16, 11]]
show_points_on_plane(list_points)
from matplotlib import pyplot as plt
import random 

def generate_random_points(number_of_points: int) -> list[list[int]]:
    points_list = []
    for i in range(number_of_points):
        points_list.append([random.randrange(-20, 20), random.randrange(-20,20)])
    return points_list

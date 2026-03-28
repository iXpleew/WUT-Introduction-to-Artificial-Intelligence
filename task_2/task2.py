from matplotlib import pyplot as plt
import random
import math 

def generate_random_points(number_of_points: int) -> list[list[int]]:
    points_list = []
    for _ in range(number_of_points):
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


def return_shortest_path(paths: list[list[list[int]]]) -> list[list[int]]:
    shortest_path = paths[0]
    shortest_path_distance = calculate_total_distance(shortest_path)
    for path in paths:
        path_distance = calculate_total_distance(path)
        if path_distance < shortest_path_distance:
            shortest_path = path
            shortest_path_distance = calculate_total_distance(shortest_path)
    return shortest_path


def shuffle_list(points:list[list[int]], shuffle_number: int) -> list[list[list[int]]]:
    combination_list = []
    starting_point = points[0]
    rest_points = points[1:]
    for _ in range(shuffle_number):
        random.shuffle(rest_points)
        combination = [starting_point] + rest_points
        combination_list.append(combination)
    return combination_list


def calculate_distribution(path: list[list[int]], sigma: float) -> float:
    path_lenght = calculate_total_distance(path)
    return math.exp(-path_lenght/sigma)


def select_random_path(shuffled_list: list[list[list[int]]], max_value: float, sigma: float) -> list[list[int]]:
    winner = random.uniform(0, max_value)

    current_fitness = 0
    for parent in shuffled_list:
        current_fitness += calculate_distribution(parent, sigma)
        if current_fitness >= winner:
            return parent
    return shuffled_list[-1]


def roulette_selection(shuffled_list: list[list[list[int]]], sigma: float, population_size: int) -> list[list[list[int]]]:
    survivors = []
    roullete_maximum = sum([calculate_distribution(x, sigma) for x in shuffled_list])
    for i in range(population_size//2):
        survivors.append(select_random_path(shuffled_list, roullete_maximum, sigma))
    return survivors


def tournament_selection(shuffled_lists: list[list[list[int]]]) -> list[list[list[int]]]:
    random.shuffle(shuffled_lists)
    mid_number = len(shuffled_lists) // 2
    survivors = []
    for i in range(mid_number):
        first_lenght = calculate_total_distance(shuffled_lists[i])
        second_lenght = calculate_total_distance(shuffled_lists[i + mid_number])
        if first_lenght < second_lenght:
            survivors.append(shuffled_lists[i])
        else:
            survivors.append(shuffled_lists[i + mid_number])
    return survivors


def create_child(first_parent: list[list[int]], second_parent: list[list[int]]):
    child = []
    cross_point = random.randint(1, len(first_parent) - 1)

    first_parent_part = first_parent[:cross_point]
    second_parent_part = [point for point in second_parent if point not in first_parent_part]
    child = first_parent_part + second_parent_part

    return child


def add_crossovers(survivors: list[list[list[int]]]) -> list[list[list[int]]]:
    children = []
    mid_number = len(survivors) // 2

    for i in range(mid_number):
        first_parent = survivors[i]
        second_parent = survivors[i + mid_number]
        
        for _ in range(2):
            child = create_child(first_parent, second_parent)
            children.append(child)
            child = create_child(second_parent, first_parent)
            children.append(child)
    return children


def add_mutations(new_generation: list[list[list[int]]], mutation_probability: int) -> list[list[list[int]]]:
    mutated_generation = []
    for path in new_generation:
        if random.randint(1, 100) < mutation_probability:
            point_a = random.randint(1, len(path) - 1)
            point_b = random.randint(1, len(path) - 1)
            path[point_a], path[point_b] = path[point_b], path[point_a]
        mutated_generation.append(path)
    return mutated_generation


def show_points_on_plane(points:list[list[int]], generation_number: int):
    x_coordinates = [x[0] for x in points]
    y_coordinates = [x[1] for x in points]
    distance = calculate_total_distance(points)
    x_coordinates.append(x_coordinates[0])
    y_coordinates.append(y_coordinates[0])
    plt.scatter(x_coordinates, y_coordinates)
    plt.plot(x_coordinates, y_coordinates)
    plt.legend([f"Total distance: {distance:.2f}", f"Generation: {generation_number}"])
    plt.show()


def optimize_path(points:list[list[int]], population: int, generation:int, sigma: int, mutation_prob: int):
    survivors = shuffle_list(points, population)
    counter = 0
    for _ in range(generation):
        survivors = roulette_selection(survivors, sigma, population)
        survivors = add_crossovers(survivors)
        survivors = add_mutations(survivors, mutation_prob)
        counter += 1

    the_best = return_shortest_path(survivors)
    show_points_on_plane(the_best, counter)

def compare_selection(points: list[list[int]], population: int, generation: int, sigma: int, mutation_prob):
    survivors_roulette = shuffle_list(points, population)
    survivors_tournament = shuffle_list(points, population)
    roulette_shortest = []
    tournament_shortest = []

    for _ in range(generation):
        survivors_tournament = tournament_selection(survivors_tournament)
        survivors_tournament = add_crossovers(survivors_tournament)
        survivors_tournament = add_mutations(survivors_tournament, mutation_prob)
        tournament_shortest.append(calculate_total_distance(return_shortest_path(survivors_tournament)))

        survivors_roulette = roulette_selection(survivors_roulette, sigma, population)
        survivors_roulette = add_crossovers(survivors_roulette)
        survivors_roulette = add_mutations(survivors_roulette, mutation_prob)
        roulette_shortest.append(calculate_total_distance(return_shortest_path(survivors_roulette)))

    plt.plot(range(len(roulette_shortest)), roulette_shortest)
    #plt.plot(range(len(tournament_shortest)), tournament_shortest)
    plt.xlabel("Generation number")
    plt.ylabel("Path distamce")
    plt.show()

if __name__ == "__main__":
    list_points = [[-14, 8], [20, 17], [13, -10], [-11, -12], [-4, 13], [-20, -12], [-4, 9], [-12, 18], [-4, -2], [-16, 11], [-3, 20], [-19, 19], [5, 0], [0, 13], [-9, -18]]
    optimize_path(list_points, 100, 200, 10, 50)

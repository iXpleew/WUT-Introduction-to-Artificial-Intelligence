from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np
import math


def get_csv_data(file_name: str) -> pd.DataFrame:
    column_names = ["Top-left", "Top", "Top-right", "Left", "Middle", "Right", "Bottom-left", "Bottom", "Bottom-right", "Target"]
    ttt_info = pd.read_csv(file_name, names=column_names).sample(frac=1, random_state=1)
    return ttt_info


def get_areas_gains(training_data: pd.DataFrame, target_column: pd.Series) -> dict[str, float]:
    information_gain_dict = {
        "Top-left": 0.0,
        "Top": 0.0,
        "Top-right": 0.0,
        "Left": 0.0,
        "Middle": 0.0,
        "Right": 0.0,
        "Bottom-left": 0.0,
        "Bottom": 0.0,
        "Bottom-right": 0.0
    }
    for index, area in enumerate(information_gain_dict.keys()):
        curr_info_gain = calculate_information_gain(training_data, training_data.iloc[:, index], target_column)
        information_gain_dict[area] = curr_info_gain
    return information_gain_dict


def calculate_entropy(data_set: pd.DataFrame, target_column: pd.Series):
    row_number = len(data_set)
    target_values = data_set[target_column.name].unique()

    entropy = 0
    for value in target_values:
        value_count = len(data_set[data_set[target_column.name] == value])
        proportion = value_count/row_number
        entropy -= proportion * math.log2(proportion)
    return entropy


def calculate_information_gain(data_set: pd.DataFrame, feature: pd.Series, target_column: pd.Series) -> float:
    parent_entropy = calculate_entropy(data_set, target_column)
    unique_values = data_set[feature.name].unique()
    weighted_entropy = 0

    for value in unique_values:
        subset = data_set[data_set[feature.name] == value]
        proportion = len(subset)/len(data_set)
        weighted_entropy += proportion * calculate_entropy(subset, target_column)
    information_gain = parent_entropy - weighted_entropy
    return information_gain


def split_data(data_set: pd.DataFrame) -> tuple:
    data_lenght = len(data_set)
    first_border = int(data_lenght * 7/10)
    second_border = int(data_lenght * 8.5/10)
    return data_set.iloc[:first_border], data_set.iloc[first_border:second_border], data_set.iloc[second_border:]


def create_tree(data: pd.DataFrame, areas: list[str], target_column: pd.Series, max_depth = 5):
    if len(data[target_column.name].unique()) == 1:
        return data[target_column.name].iloc[0]
    
    if len(areas) == 0 or max_depth == 0:
        return data[target_column.name].mode().iloc[0]
    
    best_area = max(areas, key=lambda x: calculate_information_gain(data, data[x], target_column))
    most_common_outcome = data[target_column.name].mode().iloc[0]

    tree = {best_area: {"current_optimal": most_common_outcome}}
    areas = [area for area in areas if area != best_area]
    for value in data[best_area].unique():
        subset = data[data[best_area] == value]
        tree[best_area][value] = create_tree(subset, areas, target_column, max_depth-1)
    return tree


def find_answer(tree: dict, sample_set: pd.Series):
    if isinstance(tree, str):
        return tree
    else:
        current_area = next(iter(tree.keys()))
        char_on_area = sample_set[current_area]
        if char_on_area not in tree[current_area]:
            return tree[current_area]["current_optimal"]
        else:
            return find_answer(tree[current_area][char_on_area], sample_set)


def get_confusion_matrix(tree:dict, validate_set: pd.DataFrame) -> dict:
    confusion_matrix = {
        "true_positive": 0,
        "false_positive": 0,
        "false_negative": 0,
        "true_negative": 0
    }
    validate_set = validate_set.reset_index()
    for index, prediction in validate_set.iterrows():
        model_answer = find_answer(tree, prediction)
        if model_answer == prediction["Target"] == True:
            confusion_matrix["true_positive"] += 1
        elif model_answer == prediction["Target"] == False:
            confusion_matrix["true_negative"] += 1
        elif model_answer != prediction["Target"] == True:
            confusion_matrix["false_negative"] += 1
        else:
            confusion_matrix["false_positive"] += 1
    return confusion_matrix


def print_confusion_matrix(tree: dict, validate_set: pd.DataFrame):
    matrix = get_confusion_matrix(tree, validate_set)
    print(f".             PREDICTED")
    print(f"ACTUAL  | POSITIVE | NEGATIVE ")
    print(f"POSITIVE|{matrix["true_positive"]} | {matrix["false_negative"]}")
    print(f"NEGATIVE|{matrix["false_positive"]} | {matrix["true_negative"]}")


def get_accuracy_byvalidate_data(tree: dict, validate_set: pd.DataFrame) -> float:
    correct_prediction = 0

    validate_set = validate_set.reset_index()
    for index, prediction in validate_set.iterrows():
        if find_answer(tree, prediction) == prediction["Target"]:
            correct_prediction += 1

    percentage_prediction = float("{:.2f}".format(correct_prediction/len(validate_set) * 100))
    # print(f"Model accuracy is {percentage_prediction}%")
    return percentage_prediction


def show_depth_dependency_plot(train_set: pd.DataFrame, validate_set: pd.DataFrame, areas: list[str]):
    targets = train_set.iloc[:,-1]
    accuracies = []
    for i in range(10):
        tree = create_tree(train_set, areas, targets, max_depth=i)
        accuracies.append(get_accuracy_byvalidate_data(tree, validate_set))
    plt.plot(range(10), accuracies, color="lime", marker="o")
    plt.xlabel("Max Tree Depth  allowed")
    plt.ylabel("Accuracy in %")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    provided_data = get_csv_data("task_4/tic+tac+toe+endgame/tic-tac-toe.data")
    train_set, validate_set, test_set = split_data(provided_data)

    target_values = train_set.iloc[:, -1]
    data_set_entropy = calculate_entropy(train_set, target_values)
    areas_gains = get_areas_gains(train_set, target_values)
    # tree = create_tree(train_set, list(areas_gains.keys()), target_values)
    # validate_data(tree, validate_set)

    
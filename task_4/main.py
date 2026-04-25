from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np
import math


def get_csv_data(file_name: str) -> pd.DataFrame:
    column_names = ["Top-left", "Top", "Top-right", "Left", "Middle", "Right", "Bottom-left", "Bottom", "Bottom-right", "Target"]
    ttt_info = pd.read_csv(file_name, names=column_names).sample(frac=1)
    return ttt_info


def get_areas_gains(data: pd.DataFrame, target_column: pd.Series) -> dict[str, float]:
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
        curr_info_gain = calculate_information_gain(provided_data, provided_data.iloc[:, index], target_column)
        print(f"Information Gain for {area} index is {curr_info_gain}")
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


def id3(data: pd.DataFrame, areas: list[str], target_column: pd.Series):
    if len(data[target_column.name].unique()) == 1:
        return data[target_column].iloc[0]
    
    if len(areas) == 0:
        return data[target_column].mode().iloc[0]
    
    best_area = max(areas, key=lambda x: calculate_information_gain(data, x, target_column))


if __name__ == "__main__":
    provided_data = get_csv_data("tic+tac+toe+endgame/tic-tac-toe.data")
    target_values = provided_data.iloc[:, -1]
    data_set_entropy = calculate_entropy(provided_data, target_values)
    areas_gains = get_areas_gains(provided_data, target_values)
    #id3(provided_data, list(areas_gains.keys()), target_values)
    print(provided_data.head())
from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np
import math


def get_csv_data(file_name: str) -> pd.DataFrame:
    ttt_info = pd.read_csv(file_name).sample(frac=1)
    return ttt_info


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


if __name__ == "__main__":
    provided_data = get_csv_data("tic+tac+toe+endgame/tic-tac-toe.data")
    data_set_entropy = calculate_entropy(provided_data, provided_data.iloc[:, -1])
    print(f"Entropy of data set is {data_set_entropy}")

    for i in range(9):
        curr_info_gain = calculate_information_gain(provided_data, provided_data.iloc[:, i], provided_data.iloc[:, -1])
        print(f"Information Gain for {i} index is {curr_info_gain}")
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


if __name__ == "__main__":
    provided_data = get_csv_data("tic+tac+toe+endgame/tic-tac-toe.data")
    data_set_entropy = calculate_entropy(provided_data, provided_data.iloc[:, -1])
    print(f"Entropy of data set is {data_set_entropy}")

    
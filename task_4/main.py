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
    return entropy


if __name__=="__main__":
    provided_data = get_csv_data("tic+tac+toe+endgame/tic-tac-toe.data")
    calculate_entropy(provided_data, provided_data[-1])

    
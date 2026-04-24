from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np


def get_csv_data(file_name: str) -> list[pd.DataFrame]:
    ttt_info = pd.read_csv(file_name).sample(frac=1)
    file_lenght = len(ttt_info)
    training_border = int(file_lenght * 7/10)

    training_data = ttt_info[:training_border]
    testing_data = ttt_info[training_border:]
    return [training_data, testing_data]


def calculate_entropy(data_set: pd.DataFrame, target_column: pd.Series):
    pass


if __name__=="__main__":
    df_training, df_testing = get_csv_data("tic+tac+toe+endgame/tic-tac-toe.data")
    print(f"{df_training.head()} has a lenght of {len(df_training)}")
    print("Now it's time for test:")
    print(f"{df_testing.head()} has lenght of {len(df_testing)}")

    
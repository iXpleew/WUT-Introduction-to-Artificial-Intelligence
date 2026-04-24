from matplotlib import pyplot as plt
import pandas as pd 
import numpy as np


def get_csv_data(file_name: str) -> pd.DataFrame:
    ttt_info = pd.read_csv(file_name)
    return ttt_info

if __name__=="__main__":
    df = get_csv_data("tic+tac+toe+endgame/tic-tac-toe.data")
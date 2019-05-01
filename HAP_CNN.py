from __future__ import print_function

import numpy as np
import pandas as pd


def read_data(file_path):

    column_names = [
        'experiment ID',
        'user ID',
        'activity ID',
        'start',
        'end'

    ]

    labels_df = pd.read_csv(file_path, delimiter=' ', header=None, names=column_names);

    return labels_df
if __name__ == "__main__":
    
    labels = 'HAPT Data Set/RawData/labels.txt'
    print(read_data(labels))

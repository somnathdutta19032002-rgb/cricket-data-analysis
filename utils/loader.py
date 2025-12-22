import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

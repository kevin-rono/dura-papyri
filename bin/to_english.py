import sys

import pandas as pd
from utils import to_english

sys.path.append("..")


def main():
    df = pd.read_csv("raw/data.csv")
    df["content"] = df["content"].apply(lambda x: to_english(x))
    df["subject"] = df["subject"].apply(lambda x: to_english(x))
    df.to_csv("raw/data_translated.csv")


if __name__ == "__main__":
    main()

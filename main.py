import argparse
import pandas as pd
from typing import List

def open_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)

    return df.values.tolist()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="our cute spotify experience")

    parser.add_argument("file_path", type=str, help="input path to the table")

    args = parser.parse_args()

    table = open_file(args.file_path)

    print(len(table))
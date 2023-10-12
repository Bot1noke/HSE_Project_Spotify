import argparse
import pandas as pd
from typing import List, Dict


def open_file(path: str) -> List[List[object]]:
    df = pd.read_csv(path)

    return df.values.tolist()


def get_year_stats(table: List[List[object]]) -> Dict:
    year_count = dict()
    for i in table:
        if i[1] in year_count.keys():
            year_count[i[1]] += 1
        else:
            year_count[i[1]] = 1
    return year_count


def get_most_mentioned_artist(table: List[List[object]]) -> str:
    artist_count_songs = dict()
    artist_name = ''
    mx = 0
    for i in table:
        if i[7] in artist_count_songs:
            artist_count_songs[i[7]] += 1
        else:
            artist_count_songs[i[7]] = 1
    for i, j in artist_count_songs.items():
        if j > mx:
            mx = j
            artist_name = i
    return artist_name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="our cute spotify experience")

    parser.add_argument("file_path", type=str, help="input path to the table")

    parser.add_argument("-a", "--artist", action="store_true")

    parser.add_argument("-y", "--year", action='store_true')

    args = parser.parse_args()

    table = open_file(args.file_path)

    if args.year:
        print('The amount of songs in each year:', get_year_stats(table))
    if args.artist:
        print('The most mentioned artist in the dataset:', get_most_mentioned_artist(table))
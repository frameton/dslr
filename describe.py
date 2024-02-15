import sys as sys
import os
from tools import colors, load_csv, parse_csv, loading_animation
import threading


def my_func():
    pass
    


if __name__ == "__main__":

    path = sys.argv[1]
    data = load_csv.load(path) # check file and get brut csv data
    csv_object = parse_csv.parse(data, path) # parse csv data and get a csv_object


    print("success get data")
    exit(0)
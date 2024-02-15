import sys as sys
import os
from tools import colors, load_csv, parse_csv, loading_animation
import threading

def parse_and_get_object():
    path = sys.argv[1]
    data = load_csv.load(path) # check file and get brut csv data
    csv_object = parse_csv.parse(data, path) # parse csv data and get a csv_object

    return csv_object
        

if __name__ == "__main__":

    csv_object = parse_and_get_object()

    #print(csv_object["data_list"][1])
    #print("")
    #print(csv_object["data_dic"]["Best Hand"])

    print("success get data")
    exit(0)
import pandas as pd
import os
from tools import colors, loading_animation
import time
import sys


def check_len_colums(headers, csv_data):
    dic = {}
    index = 0
    for elt in headers:
        dic[elt] = csv_data[elt].tolist()
        if index == 0:
            size = len(dic[elt])
        else:
            try:
                if len(dic[elt]) != size:
                    raise AssertionError("invalid csv.")
            except AssertionError as error:
                print(colors.clr.fb.red, "Error:", error, colors.clr.reset)
                sys.exit(1)
        index += 1
    
    return dic


def insert_data_in_list(dic, headers):
    data_list = []
    index = 0
    for elt in dic[headers[0]]:
        try:
            index2 = 0
            new_list = []
            for elt in headers:
                if pd.isna(dic[headers[index2]][index]):
                    dic[headers[index2]][index] = None
                new_list.append(dic[headers[index2]][index])
            data_list.append(new_list)
        except Exception:
                print(colors.clr.fg.yellow, f"Warning: an error occured on line {index + 2}.", colors.clr.reset)
        index += 1
    
    return data_list


def parse(csv_data, path):
    """
    Parrse data from csv file.
    """

    # start loading animation
    print("")
    loading_animation.start("Parsing " + path + "...")

    # get list of header csv
    headers = csv_data.columns.values.tolist()

    # function for check len of all column, error if different
    dic = check_len_colums(headers, csv_data)
    
    data_list = insert_data_in_list(dic, headers)
    
    # create csv_objet with all informations and data
    csv_object = {}
    csv_object["headers"] = headers
    csv_object["data"] = data_list
    csv_object["columns_len"] = len(data_list)
    csv_object["columns_number"] = len(headers)

    # stop loading animation
    loading_animation.stop()

    print(colors.clr.fg.green, "Parse success.", colors.clr.reset)
    print("")
    print("")

    return(csv_object)


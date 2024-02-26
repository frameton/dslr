import pandas as pd
from tools import colors, loading_animation
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
                index2 += 1
            data_list.append(new_list)
        except Exception:
                print(colors.clr.fg.yellow, f"Warning: an error occured on line {index + 2}.", colors.clr.reset)
        index += 1
    
    return data_list, dic


def find_type_of_column(headers, data_list):
    columns_type = {}

    index = 0
    for elt in headers:
        columns_type[elt] = type(data_list[0][index])
        index += 1

    return columns_type
    

def parse(csv_data, path):
    """
    Parrse data from csv file.
    """

    # start loading animation
    print("")
    loading_animation.start("Parsing " + path + "...")

    # get list of header csv
    headers = csv_data.columns.values.tolist()

    # function for create a dictionnary of data and check len of all column, error if different
    data_dic = check_len_colums(headers, csv_data)

    # function for create a list of data
    data_list, data_dic = insert_data_in_list(data_dic, headers)

    # function for find type of each column
    columns_type = find_type_of_column(headers, data_list)
    
    # create csv_objet with all informations and data
    csv_object = {}
    csv_object["headers"] = headers
    csv_object["data_brut"] = csv_data
    csv_object["data_list"] = data_list
    csv_object["data_dic"] = data_dic
    csv_object["columns_len"] = len(data_list)
    csv_object["columns_number"] = len(headers)
    csv_object["columns_type"] = columns_type

    # stop loading animation
    loading_animation.stop()

    print(colors.clr.fg.green, "Parse success.", colors.clr.reset)
    print("")
    print("")

    return(csv_object)


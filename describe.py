import sys as sys
import os
from tools import colors, load_csv, parse_csv, loading_animation
import threading
from decimal import Decimal
from math import sqrt, ceil


def find_max_len_elt(headers, data_dic, columns_type, columns_len):
    columns_max_elt_len = {}
    max_len = 0
    formatted = "{:.6f}".format(columns_len)

    for elt in headers:
        if columns_type[elt] is int or columns_type[elt] is float:
            column_max_len_elt = len(str(formatted))
            if len(elt) > max_len:
                max_len = len(elt)
            if len(elt) > column_max_len_elt:
                column_max_len_elt = len(elt)
            for elt2 in data_dic[elt]:
                if elt2 != None:
                    formatted2 = "{:.6f}".format(elt2)
                    if len(str(formatted2)) > column_max_len_elt:
                        column_max_len_elt = len(str(formatted2))
                    if len(str(formatted2)) > max_len:
                        max_len = len(str(formatted2))
                columns_max_elt_len[elt] = column_max_len_elt
    
    return max_len, columns_max_elt_len


def display_headers(headers, columns_elt_mlen, columns_type):
    alternate_color = True

    print(" "*5, end="")
    print(" "*4, end="")
    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):
            print(f"{color}", end="")
            print(elt, end="")
            print(" "*(columns_elt_mlen[elt] - len(elt)), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")
    print("")


def display_count(headers, columns_elt_mlen, columns_type, columns_len):
    alternate_color = True

    print("Count", end="")
    print(" "*4, end="")
    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):
            formatted = "{:.6f}".format(columns_len) 
            print(f"{color}", end="")
            print(formatted, end="")
            print(" "*(columns_elt_mlen[elt] - len(str(formatted))), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")


def display_mean(headers, columns_elt_mlen, columns_type, columns_len, data_dic):
    alternate_color = True

    print("Mean", end="")
    print(" "*5, end="")
    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):

            column_sum = 0
            for elt2 in data_dic[elt]:
                if elt2 != None:
                    column_sum += elt2
            mean = column_sum / columns_len
            formatted = "{:.6f}".format(mean) 
            print(f"{color}", end="")
            print(formatted, end="")
            print(" "*(columns_elt_mlen[elt] - len(str(formatted))), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")


def display_std(headers, columns_elt_mlen, columns_type, columns_len, data_dic):
    alternate_color = True

    print("Std", end="")
    print(" "*6, end="")
    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):

            column_sum = 0
            for elt2 in data_dic[elt]:
                if elt2 != None:
                    column_sum += elt2
            mean = column_sum / columns_len

            var_total = 0
            for elt2 in data_dic[elt]:
                if elt2 != None:
                    var_total += (elt2 - mean) ** 2
            variance = var_total / len(data_dic[elt])

            standard_deviation = sqrt(variance)
            formatted = "{:.6f}".format(standard_deviation) 
            print(f"{color}", end="")
            print(formatted, end="")
            print(" "*(columns_elt_mlen[elt] - len(str(formatted))), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")


def display_min(headers, columns_elt_mlen, columns_type, data_dic):
    alternate_color = True

    print("Min", end="")
    print(" "*6, end="")
    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):
            set_min = False
            column_min = 0
            for elt2 in data_dic[elt]:
                if elt2 != None:
                    if set_min == False:
                        column_min = elt2
                        set_min = True
                    else:
                        if elt2 < column_min:
                            column_min = elt2
            formatted = "{:.6f}".format(column_min) 
            print(f"{color}", end="")
            print(formatted, end="")
            print(" "*(columns_elt_mlen[elt] - len(str(formatted))), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")


def display_max(headers, columns_elt_mlen, columns_type, data_dic):
    alternate_color = True

    print("Max", end="")
    print(" "*6, end="")
    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):
            column_max = 0
            set_max = False
            for elt2 in data_dic[elt]:
                if elt2 != None:
                    if set_max == False:
                        column_max = elt2
                        set_max = True
                    else:
                        if elt2 > column_max:
                            column_max = elt2

            formatted = "{:.6f}".format(column_max) 
            print(f"{color}", end="")
            print(formatted, end="")
            print(" "*(columns_elt_mlen[elt] - len(str(formatted))), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")


def display_25quartile(headers, columns_elt_mlen, columns_type, columns_len, data_dic):
    alternate_color = True

    print("25%", end="")
    print(" "*6, end="")

    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):
            data_sort = sorted(data_dic[elt], key=lambda x: (x is None, x))
            q1 = columns_len / 4
            q1 = ceil(q1)
            if data_sort[q1] != None:
                formatted = "{:.6f}".format(data_sort[q1])
            else:
                formatted = data_sort[q1]
            print(f"{color}", end="")
            print(formatted, end="")
            print(" "*(columns_elt_mlen[elt] - len(str(formatted))), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")


def display_50quartile(headers, columns_elt_mlen, columns_type, columns_len, data_dic):
    alternate_color = True

    print("50%", end="")
    print(" "*6, end="")

    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):
            data_sort = sorted(data_dic[elt], key=lambda x: (x is None, x))
            if columns_len < 1:
                q2 = None
            elif (columns_len % 2 != 0):
                q2 = data_sort[int((columns_len - 1) / 2)]
            elif (columns_len % 2 == 0):
                val1 = data_sort[int(columns_len / 2)]
                val2 = data_sort[int((columns_len / 2) + 1)]
                q2 = (val1 + val2) / 2

            if q2 != None:
                formatted = "{:.6f}".format(q2)
            else:
                formatted = q2
            print(f"{color}", end="")
            print(formatted, end="")
            print(" "*(columns_elt_mlen[elt] - len(str(formatted))), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")


def display_75quartile(headers, columns_elt_mlen, columns_type, columns_len, data_dic):
    alternate_color = True

    print("75%", end="")
    print(" "*6, end="")

    for elt in headers:
        if alternate_color is True:
            color = colors.clr.fg.purple
        else:
            color = colors.clr.fg.cyan
        if elt != "Index" and (columns_type[elt] is int or columns_type[elt] is float):
            data_sort = sorted(data_dic[elt], key=lambda x: (x is None, x))
            q3 = (3 * columns_len) / 4
            q3 = ceil(q3)
            if data_sort[q3] != None:
                formatted = "{:.6f}".format(data_sort[q3])
            else:
                formatted = data_sort[q3]
            print(f"{color}", end="")
            print(formatted, end="")
            print(" "*(columns_elt_mlen[elt] - len(str(formatted))), end="")
            print(" "*4, end="")
            alternate_color = not alternate_color
    
    print(colors.clr.reset, end="")
    print("")


def parse_and_get_object():
    path = sys.argv[1]
    data = load_csv.load(path) # check file and get brut csv data
    csv_object = parse_csv.parse(data, path) # parse csv data and get a csv_object

    return csv_object
        

if __name__ == "__main__":

    csv_object = parse_and_get_object()

    #find max elt len by column and by entire csv
    max_len, csv_object["columns_elt_mlen"] = find_max_len_elt(csv_object["headers"], csv_object["data_dic"], csv_object["columns_type"], csv_object["columns_len"])


    display_headers(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"])
    display_count(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"], csv_object["columns_len"])
    display_mean(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"], csv_object["columns_len"], csv_object["data_dic"])
    display_std(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"], csv_object["columns_len"], csv_object["data_dic"])
    display_min(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"], csv_object["data_dic"])
    display_25quartile(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"], csv_object["columns_len"], csv_object["data_dic"])
    display_50quartile(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"], csv_object["columns_len"], csv_object["data_dic"])
    display_75quartile(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"], csv_object["columns_len"], csv_object["data_dic"])
    display_max(csv_object["headers"], csv_object["columns_elt_mlen"], csv_object["columns_type"], csv_object["data_dic"])

    print("")
    print("")
    exit(0)
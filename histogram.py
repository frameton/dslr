import matplotlib.pyplot as plt
import sys as sys
import os
from tools import colors, load_csv, parse_csv, loading_animation, get_csv_object
import threading
from decimal import Decimal
from math import sqrt, ceil


def histogram(csv_object):
    """
    load csv file and display graph life expectancy
    """

    data = load("life_expectancy_years.csv")
    headers = data.columns.values.tolist()
    france_elt = data.loc[data['country'] == "France"]
    years = headers[1:]
    life_expectancy = []
    for elt in years:
        life_expectancy.append(float(france_elt[elt]))
    plt.plot(csv_object["headers"], life_expectancy)
    plt.title('France Life Expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.xticks(years[::40])
    plt.show()


if __name__ == "__main__":
    csv_object = get_csv_object.get()
    histogram(csv_object)

    print("Done.")

    exit(0)
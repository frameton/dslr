import matplotlib.pyplot as plt
from tools import colors, get_csv_object
import seaborn as sbn
import pandas as pd


def pair_plot(csv_object):
    """
    display pair_plot
    """
    print(colors.clr.fg.green, "Display pair_plot...", colors.clr.reset)
    obj = csv_object["data_brut"].copy()

    for elt in csv_object["data_brut"]:
        if elt == "Index" or (csv_object["columns_type"][elt] is not int and csv_object["columns_type"][elt] is not float and elt != "Hogwarts House"):
            del obj[elt]

    obj = obj.dropna()
    obj = obj.dropna(axis=0)
    obj = obj.dropna().reset_index(drop=True)
    
    sbn.pairplot(obj, hue='Hogwarts House')
    plt.show()



if __name__ == "__main__":
    csv_object = get_csv_object.get()
    pair_plot(csv_object)

    exit(0)
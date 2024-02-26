import matplotlib.pyplot as plt
from tools import colors, get_csv_object
import seaborn as sbn
import pandas as pd


def scatter_plot(csv_object):
    """
    display pair_plot
    """
    print(colors.clr.fg.green, "Display scatter_plot...", colors.clr.reset)
    obj = csv_object["data_dic"].copy()

    index = 0
    for elt in csv_object["data_dic"]["Astronomy"]:
        if csv_object["data_dic"]["Astronomy"][index] == None or csv_object["data_dic"]["Defense Against the Dark Arts"][index] == None:
            del obj["Astronomy"][index]
            del obj["Defense Against the Dark Arts"][index]
    
    plt.scatter(obj["Defense Against the Dark Arts"], obj["Astronomy"])
    plt.title('Similar feature')
    plt.xlabel('Defense Against the Dark Arts')
    plt.ylabel('Astronomy')
    plt.show()


if __name__ == "__main__":
    csv_object = get_csv_object.get()
    scatter_plot(csv_object)

    exit(0)
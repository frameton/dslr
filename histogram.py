import matplotlib.pyplot as plt
from tools import colors, get_csv_object
 

def create_houses_dic(csv_object):
    """
    Create houses dic for display histogram
    """
    houses = {}

    for elt in csv_object["data_dic"]["Hogwarts House"]:
        if elt not in houses.keys():
            houses[elt] = {}

    for elt in csv_object["headers"]:
        if elt != "Index" and (csv_object["columns_type"][elt] is int or csv_object["columns_type"][elt] is float):
            for elt2 in houses:
                houses[elt2][elt] = []
            index = 0
            for elt3 in csv_object["data_dic"][elt]:
                if elt3 is not None:
                    houses[csv_object["data_dic"]["Hogwarts House"][index]][elt].append(elt3)
                index += 1
    
    return houses


def histogram(houses, csv_object):
    """
    display histogram
    """
    print(colors.clr.fg.green, "Display histogram...", colors.clr.reset)

    for elt in csv_object["headers"]:
        if elt != "Index" and (csv_object["columns_type"][elt] is int or csv_object["columns_type"][elt] is float):
            plt.figure()
            index = 0
            for elt2 in houses:
                plt.hist(houses[elt2][elt], bins=30, alpha=0.5, label = elt2[0:3])
            plt.legend(loc = 'upper right')
            plt.title(elt)

    plt.show()


if __name__ == "__main__":
    csv_object = get_csv_object.get()
    houses = create_houses_dic(csv_object)
    histogram(houses, csv_object)

    exit(0)
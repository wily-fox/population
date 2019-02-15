from intens import *
from save import *
from datetime import datetime



def sear(alpha, blue, red, gray, delta1, delta2, delta3):
    i = 0.06
    j = 0
    h = 0.01
    while i <= 0.130881:
        start = datetime.now()
        while j <= 0.7:
            loc = search_p(alpha, i, 1.821, j, h)
            x_list = loc[2]
            y_list = loc[3]
            for k in range(len(x_list)):
                # if x_list[k] <= 0:
                #     blue.append(j)
                #     delta1.append(i)
                #     break
                if y_list[k] <= 0:
                    red.append(j)
                    delta2.append(i)
                    break
                # if k == len(x_list) - 1:
                #     gray.append(j)
                #     delta3.append(i)
            j += 0.0002
        print("{} (elapsed {} sec.)".format(i, (datetime.now() - start).seconds))
        i += 0.0002
        j = 0


def main(alpha):
    blue = []
    red = []
    gray = []
    delta_b = []
    delta_r = []
    delta_g = []
    sear(alpha, blue, red, gray, delta_b, delta_r, delta_g)
    # matlab_export(delta_b, blue, "blue4.txt")
    matlab_export(delta_r, red, "red4.txt")
    # matlab_export(delta_g, gray, "gray2.txt")


main(0.4)

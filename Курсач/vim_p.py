from intens import *
from save import *


def sear(alpha, blue, red, gray, delta1, delta2, delta3):
    i = 0.000001
    j = 0
    h = 0.01
    while i <= 0.130881:
        while j <= 1:
            f = True
            loc = search_p(alpha, i, 1.821, j, h)
            x_list = loc[2]
            y_list = loc[3]
            for k in range(len(x_list)):
                if x_list[k] <= 0:
                    blue.append(j)
                    delta1.append(i)
                    f = False
                    break
                if y_list[k] <= 0:
                    red.append(j)
                    delta2.append(i)
                    f = False
                    break
                if f:
                    gray.append(j)
                    delta3.append(i)
            j += 0.01
        print(i)
        i += 0.001
        j = 0


def main(alpha):
    blue = []
    red = []
    gray = []
    delta_b = []
    delta_r = []
    delta_g = []
    sear(alpha, blue, red, gray, delta_b, delta_r, delta_g)
    matlab_export(delta_b, blue, "blue1.txt")
    matlab_export(delta_r, red, "red1.txt")
    matlab_export(delta_g, gray, "gray1.txt")


main(0.4)

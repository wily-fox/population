from save import *
from Search import *
from functions import *
import numpy as np
import math
from datetime import datetime


def make_data(alpha, delta, sig, h, blue, red, gray, delta1, delta2, delta3):
    x0, y0 = search_cycle(alpha, delta, h)
    x0 = x0[0]
    y0 = y0[0]
    for i in range(10000):
        n1 = np.random.normal()
        n2 = np.random.normal()
        km1 = h * f(x0, y0, alpha)
        lm1 = h * g(x0, y0, alpha, delta)
        km2 = h * f(x0 + km1 / 2, y0 + lm1 / 2, alpha)
        lm2 = h * g(x0 + km1 / 2, y0 + lm1 / 2, alpha, delta)
        km3 = h * f(x0 + km2 / 2, y0 + lm2 / 2, alpha)
        lm3 = h * g(x0 + km2 / 2, y0 + lm2 / 2, alpha, delta)
        km4 = h * f(x0 + km3, y0 + lm3, alpha)
        lm4 = h * g(x0 + km3, y0 + lm3, alpha, delta)
        x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6 + sig * n1 * math.sqrt(h)
        y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 + sig * n2 * math.sqrt(h)
        if x1 <= 0:
            blue.append(sig)
            delta1.append(delta)
            break
        if y1 <= 0:
            red.append(sig)
            delta2.append(delta)
            break
        if i == 9999:
            gray.append(sig)
            delta3.append(delta)
        x0 = x1
        y0 = y1


def main():
    red = []
    blue = []
    gray = []
    delta1 = []
    delta2 = []
    delta3 = []
    i = 0.1
    j = 0
    while i <= 0.2:
        start = datetime.now()
        while j <= 0.1:
            make_data(0.4, i, j, 0.01, blue, red, gray, delta1, delta2, delta3)
            j += 0.001
        print("{} (elapsed {} sec.)".format(i, (datetime.now() - start).seconds))
        i += 0.001
        j = 0

    matlab_export(delta2, red, "red.txt")
    matlab_export(delta1, blue, "blue.txt")
    matlab_export(delta3, gray, "gray.txt")


main()

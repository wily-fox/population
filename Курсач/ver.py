from save import *
from Search import *
from functions import *
import numpy as np
import math
from datetime import datetime


def make_data(alpha, delta, sig, h, v, blue, red, sigma):
    b = 0
    r = 0
    x0, y0 = search_cycle(alpha, delta, h)
    x0 = x0[0]
    y0 = y0[0]
    for i in range(v):
        for j in range(10000):
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
                b += 1
                break
            if y1 <= 0:
                r += 1
                break
            x0 = x1
            y0 = y1
    blue.append(b/v)
    red.append(r/v)
    sigma.append(sig)


def main(alpha, delta, v):
    k = 0.3
    blue = []
    red = []
    sigma = []
    while k <= 0.4:
        start = datetime.now()
        make_data(alpha, delta, k, 0.01, v, blue, red, sigma)
        print("{} (elapsed {} sec.)".format(k, (datetime.now() - start).seconds))
        k += 0.01
    matlab_export(sigma, blue, "blue_ver.txt")
    matlab_export(sigma, red, "red_ver.txt")


main(0.4, 0.12, 10000)

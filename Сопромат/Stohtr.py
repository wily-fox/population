import numpy as np
import math
from Search import *
from functions import *
from save import *


def search_cycle(alpha, delta, h):
    x, y = search(alpha, delta)
    x0 = x + 0.01
    y0 = y + 0.01
    xp1 = 100
    for i in range(1, 1000000):
        km1 = h*f(x0, y0, alpha)
        lm1 = h*g(x0, y0, alpha, delta)
        km2 = h*f(x0 + km1/2, y0 + lm1/2, alpha)
        lm2 = h*g(x0 + km1/2, y0 + lm1/2, alpha, delta)
        km3 = h*f(x0 + km2/2, y0 + lm2/2, alpha)
        lm3 = h*g(x0 + km2/2, y0 + lm2/2, alpha, delta)
        km4 = h*f(x0 + km3, y0 + lm3, alpha)
        lm4 = h*g(x0 + km3, y0 + lm3, alpha, delta)
        x1 = x0 + (km1 + 2*km2 + 2*km3 + km4)/6
        y1 = y0 + (lm1 + 2*lm2 + 2*lm3 + lm4)/6
        if x0 > x and x1 > x and (y0 - y)*(y1 - y) < 0:
            xp2 = x0 + (y - y0)*(x0 - x1)/(y0 - y1)
            if abs(xp1-xp2) < 1.0e-5:
                x0 = xp2
                y0 = y
                for j in range(100000):
                    km1 = h * f(x0, y0, alpha)
                    lm1 = h * g(x0, y0, alpha, delta)
                    km2 = h * f(x0 + km1 / 2, y0 + lm1 / 2, alpha)
                    lm2 = h * g(x0 + km1 / 2, y0 + lm1 / 2, alpha, delta)
                    km3 = h * f(x0 + km2 / 2, y0 + lm2 / 2, alpha)
                    lm3 = h * g(x0 + km2 / 2, y0 + lm2 / 2, alpha, delta)
                    km4 = h * f(x0 + km3, y0 + lm3, alpha)
                    lm4 = h * g(x0 + km3, y0 + lm3, alpha, delta)
                    x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6
                    y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6
                    if x0 > x and x1 > x and (y0 - y)*(y1 - y) < 0:
                        return x1, y1
                    x0 = x1
                    y0 = y1
            else:
                xp1 = xp2
        x0 = x1
        y0 = y1


def make_data(alpha, delta, sig, h):
    main_listx = []
    main_listy = []
    list_t = []
    # x0, y0 = search_cycle(alpha, delta, h)
    x0, y0 = search3(alpha, delta)
    # print(x0, y0)
    for i in range(100000):
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
        # x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6 + sig * n1 * math.sqrt(h)
        # y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 + sig * n2 * math.sqrt(h)
        if x0 <= 0:
            x1 = 0
        else:
            # x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6 + sig * n1 * math.sqrt(h)
            # x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6 + x0 * sig * n1 * math.sqrt(h)
            x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6
        if y0 <= 0:
            y1 = 0
        else:
            # y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 + sig * n2 * math.sqrt(h)
            # y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 - y0 * sig * n2 * math.sqrt(h)
            y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 - y0 * y0 * sig * n2 * math.sqrt(h)
        main_listx.append(x1)
        main_listy.append(y1)
        list_t.append(i)
        x0 = x1
        y0 = y1
    main_listx1 = []
    main_listy1 = []
    for i in range(0, len(main_listx), 10):
        main_listx1.append(main_listx[i])
        main_listy1.append(main_listy[i])
    return main_listx1, main_listy1
    # return main_listx, main_listy


x, y = make_data(0.4, 0.1309, 0.001, 0.01)
matlab_export(x, y, "tr_ag.txt")

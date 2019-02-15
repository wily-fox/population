from functions import *


def search(alpha, delta):
    node_x = list()
    node_x.append(1)
    for z in range(100000):
        x = node_x[z] - func(alpha, delta, node_x[z])/(pr_func(alpha, delta, node_x[z]))
        node_x.append(x)
        if abs(node_x[z+1] - node_x[z]) < 10**(-5):
            y = func_y(alpha, delta,  node_x[z + 1])
            return node_x[z+1], y


def search2(alpha, delta):
    node_x = list()
    node_x.append(1)
    x11 = search(alpha, delta)[0]
    for z in range(10000):
        f = (func(alpha, delta, node_x[z]) * (node_x[z] - x11) ** 2) / ((node_x[z] - x11) * (pr_func(alpha, delta, node_x[z]) * (node_x[z] - x11) - func(alpha, delta, node_x[z])))
        x = node_x[z] - f
        node_x.append(x)
        if abs(node_x[z + 1] - node_x[z]) < 10**(-5):
            y = func_y(alpha, delta, node_x[z + 1])
            return node_x[z + 1], y


def search3(alpha, delta):
    node_x = list()
    node_x.append(1)
    x11 = search(alpha, delta)[0]
    x22 = search2(alpha, delta)[0]
    for z in range(10000):
        x = \
            node_x[z] - (
                func(alpha, delta, node_x[z]) *
                (node_x[z] - x11) ** 2 *
                (node_x[z] - x22) ** 2) / (((node_x[z] - x11) * (node_x[z] - x22)) *
                                           (pr_func(alpha, delta, node_x[z]) *
                                           (node_x[z]-x11) *
                                           (node_x[z]-x22) -
                                            func(alpha, delta, node_x[z]) * (2 * node_x[z] - x22 - x11)))
        node_x.append(x)
        if abs(node_x[z+1] - node_x[z]) < 1.0e-5:
            y = func_y(alpha, delta, node_x[z + 1])
            return node_x[z+1], y


def search_cycle(alpha, delta, h):
    xnlist = []
    ynlist = []
    min_x = 200
    max_x = -200
    x, y = search(alpha, delta)
    x0 = x + 0.01
    y0 = y + 0.01
    xp1 = 100
    for i in range(1, 50000000):
        km1 = h * f(x0, y0, alpha)
        lm1 = h * g(x0, y0, alpha, delta)
        km2 = h * f(x0 + km1 / 2, y0 + lm1 / 2, alpha)
        lm2 = h * g(x0 + km1 / 2, y0 + lm1 / 2, alpha, delta)
        km3 = h * f(x0 + km2 / 2, y0 + lm2 / 2, alpha)
        lm3 = h * g(x0 + km2 / 2, y0 + lm2 / 2, alpha, delta)
        km4 = h * f(x0 + km3, y0 + lm3, alpha)
        lm4 = h * g(x0 + km3, y0 + lm3, alpha, delta)
        x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4)/6
        y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4)/6
        if x0 > x and x1 > x and (y0 - y) * (y1 - y) < 0:
            xp2 = x0 + (y - y0) * (x0 - x1) / (y0 - y1)
            if abs(xp1 - xp2) < 1.0e-5:
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
                    if x1 < min_x:
                        min_x = x1
                    if x1 > max_x:
                        max_x = x1
                    xnlist.append(x1)
                    ynlist.append(y1)
                    if x0 > x and x1 > x and (y0 - y)*(y1 - y) < 0:
                        return xnlist, ynlist
                    x0 = x1
                    y0 = y1
            else:
                xp1 = xp2
        x0 = x1
        y0 = y1
        
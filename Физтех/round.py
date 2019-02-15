from save import *


def func(alpha, delta, x):
    return -1-alpha*x+x-delta*(1+2*alpha*x+(alpha**2)*x**2-0.01*x-0.02*alpha*x**2-0.01*(alpha**2)*x**3)


def pr_func(alpha, delta, x):
    return -alpha+1-delta*(2*alpha+2*(alpha**2)*x-0.01-0.04*alpha*x-0.03*(alpha**2)*x**2)


def func_y(alpha, delta, x):
    return ((x/(1+alpha*x))-1)/delta


def f(x, y, alpha):
    return x - (x*y)/(1+alpha*x) - 0.01*x*x


def g(x, y, alpha, delta):
    return -1*y + (x*y)/(1 + alpha*x)-delta*y*y


def search(alpha, delta1):
    node_x = list()
    node_x.append(1)
    for z in range(10000):
        x = node_x[z] - func(alpha, delta1, node_x[z])/(pr_func(alpha, delta1, node_x[z]))
        node_x.append(x)
        if abs(node_x[z+1] - node_x[z]) < 10**(-5):
            y = func_y(alpha, delta1, node_x[z + 1])
            return node_x[z+1], y


def search2(alpha, delta):
    node_x = list()
    node_x.append(1)
    xy1 = search(alpha, delta)
    for z in range(1000):
        f = (func(alpha, delta, node_x[z]) * (node_x[z] - xy1[0]) ** 2) / ((node_x[z] - xy1[0]) *
             (pr_func(alpha, delta, node_x[z]) * (node_x[z] - xy1[0]) - func(alpha, delta, node_x[z])))
        x = node_x[z] - f
        node_x.append(x)
        if abs(node_x[z + 1] - node_x[z]) < 10 ** (-5):
            y = func_y(alpha, delta, node_x[z + 1])
            return node_x[z + 1], y


def search3(alpha, delta):
    node_x = list()
    node_x.append(1)
    xy1 = search(alpha, delta)
    xy2 = search2(alpha, delta)
    if xy2 is None:
        return
    for z in range(1000):
        x = node_x[z] - (func(alpha, delta, node_x[z]) * (node_x[z] - xy1[0]) ** 2 * (node_x[z] - xy2[0]) ** 2) / (
         ((node_x[z] - xy1[0]) * (node_x[z] - xy2[0]))
         * (pr_func(alpha, delta, node_x[z]) * (node_x[z] - xy1[0]) * (node_x[z] - xy2[0]) - func(alpha, delta,
            node_x[z]) * (2 * node_x[z] - xy2[0] - xy1[0])))
        node_x.append(x)
        if abs(node_x[z + 1] - node_x[z]) < 1.0e-5:
            y = func_y(alpha, delta, node_x[z + 1])
            return node_x[z + 1], y


def search_cycle(alpha, delta):
    h = 0.01
    xnlist = []
    ynlist = []
    minX = 200
    maxX = -200
    x, y = search(alpha, delta)
    x0 = x + 0.01
    y0 = y + 0.01
    xp1 = 100
    for i in range(1, 10000000):
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
                for j in range(1000000):
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
                    if x1 < minX:
                        minX = x1
                    if x1 > maxX:
                        maxX = x1
                    xnlist.append(x1)
                    ynlist.append(y1)
                    if x0 > x and x1 > x and (y0 - y)*(y1 - y) < 0:
                        t = j*h
                        return xnlist, ynlist
                        # return xnlist, ynlist, maxX, minX, t
                    x0 = x1
                    y0 = y1
            else:
                xp1 = xp2
        x0 = x1
        y0 = y1


def make_data(x, y, alpha, delta, h):
    xlist = []
    ylist = []
    for i in range(1000000):
        km1 = h*f(x, y, alpha)
        lm1 = h*g(x, y, alpha, delta)
        km2 = h*f(x + km1/2, y + lm1/2, alpha)
        lm2 = h*g(x + km1/2, y + lm1/2, alpha, delta)
        km3 = h*f(x + km2/2, y + lm2/2, alpha)
        lm3 = h*g(x + km2/2, y + lm2/2, alpha, delta)
        km4 = h*f(x + km3, y + lm3, alpha)
        lm4 = h*g(x + km3, y + lm3, alpha, delta)
        x1 = x + (km1 + 2*km2 + 2*km3 + km4)/6
        y1 = y + (lm1 + 2*lm2 + 2*lm3 + lm4)/6
        xlist.append(x1)
        ylist.append(y1)
        if abs(x1) > 100 or abs(y1) > 100:
            return xlist, ylist
        x = x1
        y = y1
    return xlist, ylist


def main(alpha, delta):
    x, y = search_cycle(alpha, delta)
    # x, y = make_data(100, 16, alpha, delta, 0.01)
    matlab_export(x, y, "kr5.txt")
    # print(len(search_cycle(alpha, 0.1308805)[0]) * 0.01)
    # print(len(search_cycle(alpha, 0.196565)[0]) * 0.01)
    # print(len(search_cycle(alpha, 0.22)[0]) * 0.01)
    # h = 0.01
    # i = 0.000001
    # T1 = []
    # T2 = []
    # del_1 = []
    # del_2 = []
    # while i <= 0.130881:
    #     T1.append(len(search_cycle(alpha, i)[0]) * h)
    #     del_1.append(i)
    #     print(i)
    #     i += 0.0001
    # i = 0.196565
    # while i <= 0.22:
    #     T2.append(len(search_cycle(alpha, i)[0]) * h)
    #     del_2.append(i)
    #     print(i)
    #     i += 0.0001
    # plt.plot(del_1, T1, del_2, T2)
    # matlab_export(del_1, T1, "T_del1.txt")
    # matlab_export(del_2, T2, "T_del2.txt")
    # h0 = 0.1
    # h1 = -0.1
    # xy1 = search(alpha, delta)
    # xy2 = search2(alpha, delta)
    # xy3 = search3(alpha, delta)
    # # x1 = xy2[0] - 0.001
    # # xs1 = xs2 = xy2[0]
    # # ys1 = xy2[1] + 0.0001
    # # ys2 = xy2[1] - 0.0001
    # # xsep1, ysep1 = make_data(xs1, ys1, alpha, delta, h1)
    # # xsep2, ysep2 = make_data(xs2, ys2, alpha, delta, h1)
    # plt.grid(True)
    # pylab.show()


if __name__ == "__main__":
    main(0.891, 0.004219)

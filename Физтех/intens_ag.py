from math import *
import numpy as np
from save import *
from sensitivity_ag import *


def search_p(alpha, delta, k, sig, h):
    x1_list = []
    y1_list = []
    x2_list = []
    y2_list = []
    m_list, x_list, y_list = sens(alpha, delta, h)
    # matlab_export(m_list, x_list, 'm_x.txt')
    for i in range(len(m_list)):
        f_zn = f(x_list[i], y_list[i], alpha)
        g_zn = g(x_list[i], y_list[i], alpha, delta)
        sq_fg = sqrt(f_zn ** 2 + g_zn ** 2)
        x1 = x_list[i] - g_zn * k * sig * sqrt(2 * m_list[i]) / sq_fg
        y1 = y_list[i] + k * sig * f_zn * sqrt(2 * m_list[i]) / sq_fg
        x2 = x_list[i] + g_zn * k * sig * sqrt(2 * m_list[i]) / sq_fg
        y2 = y_list[i] - k * sig * f_zn * sqrt(2 * m_list[i]) / sq_fg
        x1_list.append(x1)
        y1_list.append(y1)
        x2_list.append(x2)
        y2_list.append(y2)
    # matlab_export(x2_list, y2_list, "pol2.txt")
    return x1_list, y1_list, x2_list, y2_list, x_list, y_list


def make_data1(x, y, alpha, delta, h):
    xlist = [x]
    ylist = [y]
    for i in range(10000):
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
        x = x1
        y = y1
    return xlist, ylist


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
    x0, y0 = search_cycle(alpha, delta, h)
    # x0, y0 = search(alpha, delta)
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
            x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6 + x0 * sig * n1 * math.sqrt(h)
            # x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6
        if y0 <= 0:
            y1 = 0
        else:
            # y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 + sig * n2 * math.sqrt(h)
            y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 - y0 * sig * n2 * math.sqrt(h)
            # y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 - y0 * y0 * sig * n2 * math.sqrt(h)
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


def main(alpha, delta, k, sig, h):
    xy = search2(alpha, delta)
    xs1 = xs2 = xy[0]
    ys1 = xy[1] + 0.0001
    ys2 = xy[1] - 0.0001
    x1, y1, x2, y2, x3, y3 = search_p(alpha, delta, k, sig, h)
    x4, y4 = make_data(alpha, delta, sig, h)
    # print(len(x3))
    # print(search3(alpha, delta))
    xsep1, ysep1 = make_data1(xs1, ys1, alpha, delta, -0.01)
    xsep2, ysep2 = make_data1(xs2, ys2, alpha, delta, -0.01)
    matlab_export([xy[0]], [xy[1]], "rav.txt")
    matlab_export(xsep1, ysep1, "sep1.txt")
    matlab_export(xsep2, ysep1, "sep2.txt")
    matlab_export(x1, y1, "pol_12_del.txt")
    matlab_export(x2, y2, "pol_22_del.txt")
    matlab_export(x3, y3, "cycle_del.txt")
    matlab_export(x4, y4, "traekt_del.txt")
    # plt.plot(x4, y4, 'o')# c='#808080', ls=':')
    #plt.plot(x1, y1, 'b', x2, y2, 'r', x3, y3, 'k')
    # plt.plot(xsep1, ysep1, 'r:', xsep2, ysep2, 'r:')
    #plt.axis([-5, 120, -5, 15])
    #plt.grid(True)
    #pylab.show()


if __name__ == '__main__':
    main(0.4, 0.21, 1.821, 0.004, 0.01)

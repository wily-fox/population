from math import *
from Stohtr import *
from save import *
from sensitivity import *


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
        if abs(x1) > 100 or abs(y1) > 100:
            return xlist, ylist
        xlist.append(x1)
        ylist.append(y1)
        x = x1
        y = y1
    return xlist, ylist


def main(alpha, delta, k, sig, h):
    # xy = search2(alpha, delta)
    #xs1 = xs2 = xy[0]
    #ys1 = xy[1] + 0.0001
    # ys2 = xy[1] - 0.0001
    x1, y1, x2, y2, x3, y3 = search_p(alpha, delta, k, sig, h)
    x4, y4 = make_data(alpha, delta, sig, h)
    print(len(x3))
    # xsep1, ysep1 = make_data1(xs1, ys1, alpha, delta, -0.01)
    # xsep2, ysep2 = make_data1(xs2, ys2, alpha, delta, -0.01)
    # matlab_export(xsep1, ysep1, "sep1.txt")
    # matlab_export(xsep2, ysep1, "sep2.txt")
    # matlab_export(x1, y1, "pol_12.txt")
    matlab_export(x2, y2, "pol_22.txt")
    matlab_export(x3, y3, "cycle.txt")
    matlab_export(x4, y4, "traekt.txt")
    plt.plot(x4, y4, 'o')# c='#808080', ls=':')
    plt.plot(x1, y1, 'b', x2, y2, 'b', x3, y3, 'k')
    # plt.plot(xsep1, ysep1, 'r:', xsep2, ysep2, 'r:')
    plt.axis([-5, 120, -5, 15])
    plt.grid(True)
    pylab.show()


if __name__ == '__main__':
    main(0.4, 0.12, 1.821, 0.05, 0.01)

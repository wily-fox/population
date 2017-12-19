from Search import *
import math
import pylab
import matplotlib.pyplot as plt
from save import *


def sustainability(alpha, delta):
    x_list, y_list = search_cycle(alpha, delta)
    h = 0.01
    k = len(x_list)
    z11 = 1
    z12 = 0
    z21 = 0
    z22 = 1
    for i in range(k):
        zn11 = z11 + h * pr_f_x(alpha, x_list[i], y_list[i]) * z11 + h * pr_f_y(alpha, x_list[i]) * z12
        zn12 = z12 + h * pr_g_x(alpha, x_list[i], y_list[i]) * z11 + h * pr_g_y(alpha, delta, x_list[i], y_list[i]) * z12
        zn21 = z21 + h * pr_f_x(alpha, x_list[i], y_list[i]) * z21 + h * pr_f_y(alpha, x_list[i]) * z22
        zn22 = z22 + h * pr_g_x(alpha, x_list[i], y_list[i]) * z21 + h * pr_g_y(alpha, delta, x_list[i], y_list[i]) * z22
        z11 = zn11
        z12 = zn12
        z21 = zn21
        z22 = zn22
    p2 = z11 * z22 - z21 * z12
    # print(p2)
    if math.fabs(p2) < 1:
        print(delta, 'OK')
    if p2 == 0:
        lam_r = -1
    else:
        lam_r = math.log(math.fabs(p2))/(k * h)
    return delta, lam_r


def sensitivity(alpha, delta):
    mas_r = []
    mas_h = []
    r1 = 1
    h1 = 0
    mas_r.append(r1)
    mas_h.append(h1)
    x_list, y_list = search_cycle(alpha, delta)



def make_data(alpha):
    i = 0.000001
    delta1 = []
    lambda1 = []
    delta2 = []
    lambda2 = []
    while i <= 0.130881:
        d1, l1 = sustainability(alpha, i)
        delta1.append(d1)
        lambda1.append(l1)
        i += 0.001
    i = 0.196565
    while i <= 0.22:
        d2, l2 = sustainability(alpha, i)
        delta2.append(d2)
        lambda2.append(l2)
        i += 0.001
    matlab_export(delta1, lambda1, 'ust3.txt')
    matlab_export(delta2, lambda2, 'ust4.txt')
    plt.plot(delta1, lambda1, 'k', delta2, lambda2, 'k')
    plt.grid(True)
    pylab.show()


if __name__ == '__main__':
    make_data(0.4)

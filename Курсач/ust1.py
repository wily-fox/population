from Search import *
import math
import pylab
import matplotlib.pyplot as plt
from save import *


def search_lambda(alpha, delta):
    x_list, y_list = search_cycle(alpha, delta, 0.01)
    li = 0
    h = 0.01
    for i in range(len(x_list)):
        ft = pr_f_x(alpha, x_list[i], y_list[i])
        gt = pr_g_y(alpha, delta, x_list[i], y_list[i])
        li = li + h * (ft + gt)

    lambda1 = li/(len(x_list) * h)
    return lambda1


def make_data(alpha):
    print(search_lambda(alpha, 0.19656411))
    i = 0.000001
    delta1 = []
    lambda1 = []
    delta2 = []
    lambda2 = []
    while i <= 0.130881:
        delta1.append(i)
        lambda1.append(search_lambda(alpha, i))
        i += 0.001
        print(i)
    i = 0.196565
    while i <= 0.22:
        delta2.append(i)
        lambda2.append(search_lambda(alpha, i))
        i += 0.001
        print(i)
    matlab_export(delta1, lambda1, 'ust1.txt')
    matlab_export(delta2, lambda2, 'ust2.txt')
    plt.plot(delta1, lambda1, 'k', delta2, lambda2, 'k')
    plt.grid(True)
    pylab.show()


if __name__ == '__main__':
    make_data(0.4)






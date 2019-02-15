import sensitivity
import ellips
import pylab
import matplotlib.pyplot as plt
import math
from save import *


def main(alpha, h):
    T1 = []
    T2 = []
    delta_l1 = []
    delta_l2 = []
    delta_r1 = []
    delta_r3 = []
    delta_r5 = []
    max_m1 = []
    max_m2 = []
    min_m1 = []
    min_m2 = []
    rav1_1 = []
    rav1_2 = []
    rav2_1 = []
    rav2_2 = []
    rav3_1 = []
    rav3_2 = []
    rav4_1 = []
    rav4_2 = []
    rav5_1 = []
    rav5_2 = []
    i = 0.000001
    while i <= 0.130881:
        new_m, M, m, len_x = sensitivity.sens(alpha, i, h)
        T1.append(len_x * h)
        delta_l1.append(i)
        max_m1.append(M)
        min_m1.append(m)
        i += 0.001
        print(i)

    # i = 0.130881
    # while i <= 0.196565:
    #     rav1, rav2 = ellips.matr(alpha, i, 3)
    #     rav1_1.append(rav1)
    #     rav1_2.append(rav2)
    #     delta_r1.append(i)
    #     print(i)
    #     i += 0.001
    i = 0.196565
    while i <= 0.22:
        new_m, M, m, len_x = sensitivity.sens(alpha, i, h)
        T2.append(len_x * h)
        delta_l2.append(i)
        max_m2.append(M)
        min_m2.append(m)
        rav1, rav2 = ellips.matr(alpha, i, 3)
        rav2_1.append(rav1)
        rav2_2.append(rav2)
        i += 0.001
        print(i)
    i = 0.22
    # while i <= 0.239456:
    #     delta_r3.append(i)
    #     rav1, rav2 = ellips.matr(alpha, i, 1)
    #     rav3_1.append(rav1)
    #     rav3_2.append(rav2)
    #     rav1, rav2 = ellips.matr(alpha, i, 3)
    #     rav4_1.append(rav1)
    #     rav4_2.append(rav2)
    #     print(i)
    #     i += 0.001
    # while i <= 0.3:
    #     delta_r5.append(i)
    #     rav1, rav2 = ellips.matr(alpha, i, 1)
    #     rav5_1.append(rav1)
    #     rav5_2.append(rav2)
    #     print(i)
    #     i += 0.001

    # plt.plot(delta_l1, max_m1, 'b', delta_l1, min_m1, 'r', delta_l2, max_m2, 'b', delta_l2, min_m2, 'r')
    # plt.plot(delta_r1, rav1_1, 'k')
    # plt.plot(delta_r1, rav1_2, c='#A52A2A')
    # plt.plot(delta_l2, rav2_1, 'k')
    # plt.plot(delta_l2, rav2_2, c='#A52A2A')
    # plt.plot(delta_r3, rav3_1, '#008000')
    # plt.plot(delta_r3, rav3_2, c='#FFA500')
    # plt.plot(delta_r3, rav4_1, 'k')
    # plt.plot(delta_r3, rav4_2, c='#A52A2A')
    # plt.plot(delta_r5, rav5_1, 'k')
    # plt.plot(delta_r5, rav5_2, c='#A52A2A')
    # plt.plot(delta_l2, max_m2, delta_l2, min_m2)
    # plt.axis([0, 0.23, -10, 1700])
    # plt.plot(delta_l1, T1, delta_l2, T2)
    # plt.grid(True)
    # pylab.show()
    # matlab_export(delta_r1, rav1_1, "rav1_1.txt")
    # matlab_export(delta_r1, rav1_2, "rav1_2.txt")
    # matlab_export(delta_l2, rav2_1, "rav2_1.txt")
    # matlab_export(delta_l2, rav2_2, "rav2_2.txt")
    # matlab_export(delta_r3, rav3_1, "rav3_1.txt")
    # matlab_export(delta_r3, rav3_2, "rav3_2.txt")
    # matlab_export(delta_r3, rav4_1, "rav4_1.txt")
    # matlab_export(delta_r3, rav4_2, "rav4_2.txt")
    # matlab_export(delta_r5, rav5_1, "rav5_1.txt")
    # matlab_export(delta_r5, rav5_2, "rav5_2.txt")
    # matlab_export(delta_l1, max_m1, "max_m1.txt")
    # matlab_export(delta_l2, max_m2, "max_m2.txt")
    # matlab_export(delta_l1, min_m1, "min_m1.txt")
    # matlab_export(delta_l2, min_m2, "min_m2.txt")




if __name__ == '__main__':
    main(0.4, 0.01)

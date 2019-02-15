from Search import *
import math
from save import *
# import pylab
# import matplotlib.pyplot as plt


def A(x, y, alpha, delta):
    f_zn = f(x, y, alpha)
    g_zn = g(x, y, alpha, delta)
    f_x = pr_f_x(alpha, x, y)
    f_y = pr_f_y(alpha, x)
    g_x = pr_g_x(alpha, x, y)
    g_y = pr_g_y(alpha, delta, x, y)
    pr_fg = f_y + g_x
    sq_fg = f_zn ** 2 + g_zn ** 2
    return 2 * (f_x * g_zn ** 2 + g_y * f_zn ** 2 - g_zn * f_zn * pr_fg) / sq_fg

    
def b(x, y, alpha, delta):
    f_zn = f(x, y, alpha)
    g_zn = g(x, y, alpha, delta)
    sq_fg = f_zn ** 2 + g_zn ** 2
    # return ((g_zn * x) ** 2 + (f_zn * y) ** 2)/sq_fg
    return ((f_zn * y * y) ** 2) / sq_fg
    

def sens(alpha, delta, h):
    max_m = 0
    min_m = 1000
    x_list, y_list = search_cycle(alpha, delta, h)
    k = len(x_list)
    # print(k)
    h_list = []
    r_list = []
    m_list = []
    t_list = []
    t1_list = []
    new_a = 0
    r_list.append(1)
    h_list.append(0)
    for i in range(1, k):
        a1 = A(x_list[i-1], y_list[i-1], alpha, delta)
        a2 = A(x_list[i], y_list[i], alpha, delta)
        # f_zn1 = f(x_list[i-1], y_list[i-1], alpha)
        # f_zn2 = f(x_list[i], y_list[i], alpha)
        # g_zn1 = g(x_list[i-1], y_list[i-1], alpha, delta)
        # g_zn1 = g(x_list[i - 1], y_list[i - 1], alpha, delta)
        # f_x = pr_f_x(alpha, x_list[i], y_list[i])
        # f_y = pr_f_y(alpha, x_list[i])
        # g_x = pr_g_x(alpha, x_list[i], y_list[i])
        # g_y = pr_g_y(alpha, delta, x_list[i], y_list[i])
        # pr_fg = f_y + g_x
        # sq_fg = f_zn ** 2 + g_zn ** 2
        # new_a += 2 * (f_x * g_zn ** 2 + g_y * f_zn ** 2 - g_zn * f_zn * pr_fg) * h / sq_fg
        new_a += (a1 + a2) * h / 2
        new_r = math.exp(new_a)
        r_list.append(new_r)
        new_h = h_list[i - 1] + h * (b(x_list[i - 1], y_list[i - 1], alpha, delta) / r_list[i - 1] + b(x_list[i], y_list[i], alpha, delta) / r_list[i]) / 2
        h_list.append(new_h)
        t1_list.append(i)
    const_c = r_list[- 1] * h_list[- 1] / (1 - r_list[- 1])
    # print(const_c)
    for i in range(k):
        m_list.append(r_list[i] * (const_c + h_list[i]))
        if m_list[i] < min_m:
            min_m = m_list[i]
        if m_list[i] > max_m:
            max_m = m_list[i]
        t_list.append(i)
    # matlab_export(r_list, h_list, "r_h.txt")
    # return m_list, t_list
    return m_list, max_m, min_m, len(x_list)

    # print(max_m, min_m)
    # return m_list, x_list, y_list


def main(alpha, delta, h):
    s, M, m, d = sens(alpha, delta, h)
    print(M, m, d)
    # x0, y0 = sens(alpha, delta, h)
    # plt.plot(x0, y0)
    # plt.grid(True)
    # pylab.show()


if __name__ == '__main__':
    main(0.4, 0.1307, 0.01)

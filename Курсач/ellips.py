from Stohtr import *
from functions import *
import math


def matr(alpha, delta, f):
    lam_1 = []
    lam_2 = []
    s = np.array([-1, 0, 0, -1])
    xy = []
    if f == 1:
        xy = search(alpha, delta)
    if f == 3:
        xy = search3(alpha, delta)
    x = xy[0]
    y = xy[1]
    fx = pr_f_x(alpha, x, y)
    fy = pr_f_y(alpha, x)
    gx = pr_g_x(alpha, x, y)
    gy = pr_g_y(alpha, delta, x, y)
    k = np.array([[2 * fx, fy, fy, 0], [gx, gy + fx, 0, fy], [gx, 0, fx + gy, fy],
                  [0, gx, gx, 2 * gy]])

    w11 = (1 - 0.02 * x + (alpha * x * y) / (1 + alpha * x) ** 2 - (y / (1 + alpha * x))) * 2
    w12 = - (x / (1 + alpha * x))
    w13 = - (x / (1 + alpha * x))

    w21 = -((alpha * x * y)/(1 + alpha * x) ** 2) + y/(1 + alpha * x)
    w22 = (1 - 0.02 * x + (alpha * x * y)/(1 + alpha * x) ** 2 - y/(1 + alpha * x)) + (-1) + x/(1 + alpha * x) - 2 * delta * y
    w24 = -(x / (1 + alpha * x))

    w31 = -((alpha * x * y)/(1 + alpha * x) ** 2) + y/(1 + alpha * x)
    w33 = 1 - 0.02 * x + (alpha * x * y)/(1 + alpha * x) ** 2 - y/(1 + alpha * x) + -1 + x/(1 + alpha * x) - 2 * delta * y
    w34 = - (x/(1 + alpha * x))

    w42 = -((alpha * x * y)/(1 + alpha * x) ** 2) + y/(1 + alpha * x)
    w43 = -((alpha * x * y)/(1 + alpha * x) ** 2) + y/(1 + alpha * x)
    w44 = 2 * (-1 + x/(1 + alpha * x) - 2 * delta * y)

    k1 = np.array([[w11, w12, w13, 0], [w21, w22, 0, w24], [w31, 0, w33, w34], [0, w42, w43, w44]])
    resolve = np.linalg.solve(k1, s)
    resolve = np.array([[resolve[0], resolve[1]], [resolve[2], resolve[3]]])
    lv, v = np.linalg.eig(resolve)
    lam_1.append(lv[0])
    lam_2.append(lv[1])
    return lam_1, lam_2


print(matr(0.4, 0.239456, 1))
# def main(alpha):
#     lambda_1 = []
#     lambda_2 = []
#     delta1 = []
#     i = 0.22
#     while i <= 0.239456:
#         matr(alpha, i, lambda_1, lambda_2)
#         delta1.append(i)
#         print(i)
#         i += 0.000001
#     plt.plot(delta1, lambda_1, delta1, lambda_2)
#     plt.grid(True)
#     pylab.show()
#
#
# main(0.4)

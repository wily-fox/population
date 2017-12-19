from Stohtr import *
from functions import *
import pylab
import matplotlib.pyplot as plt
import math
from save import *


def matr(alpha, delta):
    s = np.array([-1, 0, 0, -1])
    xy = search(alpha, delta)
    print(xy)
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
    print(lv, v)
    return lv, v, xy
   # mas_d.append(lv[2:])


def ellips(alpha, delta, sig, p):
    list_x = []
    list_y = []
    lv, v, xy = matr(alpha, delta)
    k2 = -math.log(1-p)
    lv1 = lv[0]
    lv2 = lv[1]
    v21 = v[0][1]
    v22 = v[1][1]
    v11 = v[0][0]
    v12 = v[1][0]
    x = xy[0]
    y = xy[1]
    i = 0
    # print(lv1, k2)
    while i <= 2 * math.pi:
        z1 = sig * math.sqrt(2 * k2 * lv1) * math.cos(i)
        z2 = sig * math.sqrt(2 * k2 * lv2) * math.sin(i)
        xf = x + (z1 * v22 - z2 * v12)/(v11 * v22 - v12 * v21)
        yf = y + (z2 * v11 - z1 * v21)/(v11 * v22 - v12 * v21)
        list_x.append(xf)
        list_y.append(yf)
        i += 2 * math.pi / 360
    return list_x, list_y


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


def main(alpha, delta):
    xy = search2(alpha, delta)
    xs1 = xs2 = xy[0]
    ys1 = xy[1] + 0.0001
    ys2 = xy[1] - 0.0001
    # print(xy)
    x_list, y_list = ellips(alpha, delta, 0.01, 0.99)
    obl_x, obl_y = make_data(alpha, delta, 0.01, 0.01)
    matlab_export(x_list, y_list, "ellips.txt")
    matlab_export(obl_x, obl_y, "tr.txt")
    xsep1, ysep1 = make_data1(xs1, ys1, alpha, delta, -0.01)
    xsep2, ysep2 = make_data1(xs2, ys2, alpha, delta, -0.01)
    matlab_export(xsep1, ysep1, "sep1.txt")
    matlab_export(xsep2, ysep2, "sep2.txt")
    plt.plot(x_list, y_list, 'k', obl_x, obl_y, 'o')
    plt.plot(xsep1, ysep1, 'r:', xsep2, ysep2, 'r:')
    plt.axis([0, 90, 0, 12])
    plt.grid(True)
    pylab.show()


if __name__ == '__main__':
    main(0.4, 0.1309)




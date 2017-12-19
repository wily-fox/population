import pylab
import matplotlib.pyplot as plt
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


def search(alpha, delta1, mas_x, mas_y, mas_d):
    node_x = list()
    node_x.append(1)
    for z in range(1000):
        x = node_x[z] - func(alpha, delta1, node_x[z])/(pr_func(alpha, delta1, node_x[z]))
        node_x.append(x)
        if abs(node_x[z+1] - node_x[z]) < 10**(-5):
            mas_x.append(node_x[z + 1])
            mas_d.append(delta1)
            mas_y.append(func_y(alpha, delta1, node_x[z + 1]))
            return node_x[z+1]


def search2(alpha, delta1, mas_x, mas_y, mas_d):
    node_x = list()
    node_x.append(1)
    x11 = x1[len(x1)-1]
    for z in range(1000):
        f = (func(alpha, delta1, node_x[z])*(node_x[z]-x11)**2)/((node_x[z]-x11)
                    * (pr_func(alpha, delta1, node_x[z])*(node_x[z]-x11)-func(alpha, delta1, node_x[z])))
        x = node_x[z]-f
        node_x.append(x)
        if abs(node_x[z+1] - node_x[z]) < 10**(-5):
            mas_x.append(node_x[z + 1])
            mas_d.append(delta1)
            mas_y.append(func_y(alpha, delta1, node_x[z + 1]))
            return node_x[z + 1]


def search3(alpha, delta1, mas_x, mas_y, mas_d):
    node_x = list()
    node_x.append(1)
    x11 = x1[len(x1)-1]
    x22 = x2[len(x2)-1]
    for z in range(1000):
        x = node_x[z] - (func(alpha, delta1, node_x[z])*(node_x[z]-x11)**2*(node_x[z]-x22)**2)/(((node_x[z]-x11)*(node_x[z]-x22))
                        * (pr_func(alpha, delta1, node_x[z]) *
                          (node_x[z]-x11)*(node_x[z]-x22)-func(alpha, delta1, node_x[z])*(2*node_x[z]-x22-x11)))
        node_x.append(x)
        if abs(node_x[z+1] - node_x[z]) < 1.0e-5:
            mas_x.append(node_x[z + 1])
            mas_d.append(delta1)
            mas_y.append(func_y(alpha, delta1, node_x[z + 1]))
            return node_x[z + 1]


def searchC(alpha, delta1):
    node_x = list()
    node_x.append(1)
    for z in range(10000):
        x = node_x[z] - func(alpha, delta1, node_x[z])/(pr_func(alpha, delta1, node_x[z]))
        node_x.append(x)
        if abs(node_x[z+1] - node_x[z]) < 10**(-5):
            y = func_y(alpha, delta1, node_x[z + 1])
            return node_x[z+1], y


def search_cycle(alpha, delta, minnx, maxnx):
    h = 0.01
    xnlist = []
    ynlist = []
    minX = 200
    maxX = -200
    x, y = searchC(alpha, delta)
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
                    if x1 < minX:
                        minX = x1
                    if x1 > maxX:
                        maxX = x1
                    xnlist.append(x1)
                    ynlist.append(y1)
                    if x0 > x and x1 > x and (y0 - y)*(y1 - y) < 0:
                        period.append(j * h)
                        minnx.append(minX)
                        maxnx.append(maxX)
                        return xnlist, ynlist
                    x0 = x1
                    y0 = y1
            else:
                xp1 = xp2
        x0 = x1
        y0 = y1

min1X = []
max1X = []
min2X = []
max2X = []
period = []
x0 = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
deltaX0 = []
deltaX1 = []
deltaX2 = []
deltaX3 = []
deltaX4 = []
deltaX5 = []
deltaX6 = []
deltaX7 = []
deltaX8 = []
y0 = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
i = 0.000001
while i < 0.130881:
    search(0.4, i, x0, y0, deltaX0)
    search_cycle(0.4, i, min1X, max1X)
    i += 0.01
    print('0 ', i)

i = 0.130881
while i < 0.22:
    search(0.4, i, x1, y1, deltaX1)
    search2(0.4, i, x2, y2, deltaX2)
    search3(0.4, i, x3, y3, deltaX3)
    i += 0.000001
    print('1 ', i)

i = 0.196565
while i <= 0.22:
    search_cycle(0.4, i, min2X, max2X)
    deltaX8.append(i)
    i += 0.001
    print('2 ', i)

i = 0.22
while i <= 0.239456:
    search(0.4, i, x4, y4, deltaX4)
    search2(0.4, i, x5, y5, deltaX5)
    search3(0.4, i, x6, y6, deltaX6)
    i += 0.000001
    print('3 ', i)

i = 0.239457
while i <= 0.3:
    search(0.4, i, x7, y7, deltaX7)
    i += 0.000001
    print('4 ', i)


# main_list_x = x0 + x1 + x2 + x3 + x4
# main_list_y = y0 + y1 + y2 + y3 + y4
# main_list_delta = deltaX0 + deltaX1 + deltaX2 + deltaX3 + deltaX4

# with open('coord.txt', 'w') as f:
#     for i in range(len(main_list_x) - 1):
#          f.write('{} {} {}\n'.format(round(main_list_x[i], 7), round(main_list_y[i], 7), round(main_list_delta[i], 7)))
# delta = deltaX0 + deltaX1 + deltaX2 + deltaX3 + deltaX4
# deltaX01 = np.array(deltaX0)
# deltaX8 = np.array(deltaX8)
# min1X = np.array(min1X)
# min2X = np.array(min2X)
# max1X = np.array(max1X)
# max2X = np.array(max2X)
print(len(deltaX0), len(min1X), len(max1X))
# plt.plot(deltaX0, x0, 'r')
# plt.plot(deltaX1, x1, 'r')
# plt.plot(deltaX2, x2, 'r')
# plt.plot(deltaX3, x3, 'b')
# plt.plot(deltaX4, x4, 'b')
# plt.plot(deltaX5, x5, 'r')
# plt.plot(deltaX6, x6, 'b')
# plt.plot(deltaX7, x7, 'b')
# plt.plot(deltaX0, min1X, 'k')
# plt.plot(deltaX0, max1X, 'k')
# plt.plot(deltaX8, min2X, 'k')
# plt.plot(deltaX8, max2X, 'k')
matlab_export(deltaX0, x0, "0.txt")
matlab_export(deltaX1, x1, "1.txt")
matlab_export(deltaX2, x2, "2.txt")
matlab_export(deltaX3, x3, "3.txt")
matlab_export(deltaX4, x4, "4.txt")
matlab_export(deltaX5, x5, "5.txt")
matlab_export(deltaX6, x6, "6.txt")
matlab_export(deltaX7, x7, "7.txt")
matlab_export(deltaX0, min1X, "8.txt")
matlab_export(deltaX0, max1X, "9.txt")
matlab_export(deltaX8, min2X, "10.txt")
matlab_export(deltaX8, max2X, "11.txt")
# plt.axis([0, 90, 0, 20])
plt.xlabel(r'$delta$')
plt.ylabel(r'$X$')
plt.title(r'$3 равновесия$')
plt.grid(True)
pylab.show()

# plt.plot(deltaX0, y0, deltaX1, y1, deltaX2, y2, deltaX3, y3, deltaX4, y4)
# plt.xlabel(r'$delta$')
# plt.ylabel(r'$Y$')
# plt.title(r'$3 равновесия$')
# plt.grid(True)
# pylab.show()

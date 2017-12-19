import pylab
import matplotlib.pyplot as plt



def func(alpha, delta, x):
    return -1-alpha*x+x-delta*(1+2*alpha*x+(alpha**2)*x**2-0.01*x-0.02*alpha*x**2-0.01*(alpha**2)*x**3)


def pr_func(alpha, delta, x):
    return -alpha+1-delta*(2*alpha+2*(alpha**2)*x-0.01-0.04*alpha*x-0.03*(alpha**2)*x**2)


def func_y(alpha, delta, x):
    return ((x/(1+alpha*x))-1)/delta


def f(alpha, delta, x, y):
    return x - x*y/(1+alpha*x) - 0.01*x*x


def g(alpha, delta, x, y):
    return -y + x*y/(1+alpha*x) - delta*y*y


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


def searchrk(alpha, delta, x, y):
    node_x = []
    node_y = []
    dx, dy = (x, y)
    h = -0.01
    for i in range(100000):
        km1 = h*f(alpha, delta, dx, dy)
        lm1 = h*g(alpha, delta, dx, dy)
        km2 = h*f(alpha, delta, dx + km1/2, dy + lm1/2)
        lm2 = h*g(alpha, delta, dx + km1/2, dy + lm1/2)
        km3 = h*f(alpha, delta, dx + km2/2, dy + lm2/2)
        lm3 = h*g(alpha, delta, dx + km2/2, dy + lm2/2)
        km4 = h*f(alpha, delta, dx + km3, dy + lm3)
        lm4 = h*g(alpha, delta, dx + km3, dy + lm3)
        x1 = dx + (km1 + 2*km2 + 2*km3 + km4)/6
        y1 = dy + (lm1 + 2*lm2 + 2*lm3 + lm4)/6
        print(x1, y1)
        node_x.append(x1)
        node_y.append(y1)
        if abs(x1) > 100 or abs(y1) > 100:
            return node_x, node_y
        dx = x1
        dy = y1
    return node_x, node_y

#два поиска, находим М2, две стартовые точки: +-0.00001 к у, строим КРАСНЫМ!!! можно добавить и в round
m2 = search2(0.4, 0.15)
x1 = x2 = m2[0]
y1 = m2[1] + 0.00001
y2 = m2[1] - 0.00001

x0, y0 = searchrk(0.4, 0.15, x1, y1)
x3, y3 = searchrk(0.4, 0.15, x2, y2)
plt.plot(x0, y0, 'r:', x3, y3, 'r:')
plt.grid(True)
pylab.show()

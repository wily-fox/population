import pylab
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import os


def m_x(a1, a2, b1, b2, e1, e2, d1, d2):
    return -((a1 + b1 - a2 * b1 * d2 + a1 * b2 * d2 - a2 * e1 - b2 * e1) / (-1 - b1 * d1 - 
        b2 * d2 + b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2))

  
def m_y(a1, a2, b1, b2, e1, e2, d1, d2):
    return -(a2 + b2 + a2 * b1 * d1 - a1 * b2 * d1 - a1 * e2 - b1 * e2)/(-1 - b1 * d1 - b2 * d2 + 
        b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2)
 

def m_z(a1, a2, b1, b2, e1, e2, d1, d2):
    return -((-1 + a1 * d1 + a2 * d2 - a2 * d1 * e1 - a1 * d2 * e2 + e1 * e2)/(-1 - b1 * d1 - 
        b2 * d2 + b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2))

        
def make_data(x, y, z, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2):
    h = 0.01
    xlist = []
    ylist = []
    zlist = []
    for i in range(10000):
        km1 = h * f(x, y, z, alpha1, beta1, eps1)
        lm1 = h * g(x, y, z, alpha2, beta2, eps2)
        nm1 = h * h3(x, y, z, delta1, delta2)
        km2 = h * f(x + km1/2, y + lm1/2, z + nm1/2, alpha1, beta1, eps1)
        lm2 = h * g(x + km1/2, y + lm1/2, z + nm1/2, alpha2, beta2, eps2)
        nm2 = h * h3(x + km1/2, y + lm1/2, z + nm1/2, delta1, delta2)
        km3 = h * f(x + km2/2, y + lm2/2, z + nm2/2, alpha1, beta1, eps1)
        lm3 = h * g(x + km2/2, y + lm2/2, z + nm2/2, alpha2, beta2, eps2)
        nm3 = h * h3(x + km2/2, y + lm2/2, z + nm2/2, delta1, delta2)
        km4 = h * f(x + km3, y + lm3, z + nm3, alpha1, beta1, eps1)
        lm4 = h * g(x + km3, y + lm3, z + nm3, alpha2, beta2, eps2)
        nm4 = h * h3(x + km3, y + lm3, z + nm3, delta1, delta2)
        x1 = x + (km1 + 2 * km2 + 2 * km3 + km4)/6
        y1 = y + (lm1 + 2 * lm2 + 2 * lm3 + lm4)/6
        z1 = z + (nm1 + 2 * nm2 + 2 * nm3 + nm4)/6
        x = x1
        y = y1
        z = z1
    for i in range(10000):
        km1 = h * f(x, y, z, alpha1, beta1, eps1)
        lm1 = h * g(x, y, z, alpha2, beta2, eps2)
        nm1 = h * h3(x, y, z, delta1, delta2)
        km2 = h * f(x + km1/2, y + lm1/2, z + nm1/2, alpha1, beta1, eps1)
        lm2 = h * g(x + km1/2, y + lm1/2, z + nm1/2, alpha2, beta2, eps2)
        nm2 = h * h3(x + km1/2, y + lm1/2, z + nm1/2, delta1, delta2)
        km3 = h * f(x + km2/2, y + lm2/2, z + nm2/2, alpha1, beta1, eps1)
        lm3 = h * g(x + km2/2, y + lm2/2, z + nm2/2, alpha2, beta2, eps2)
        nm3 = h * h3(x + km2/2, y + lm2/2, z + nm2/2, delta1, delta2)
        km4 = h * f(x + km3, y + lm3, z + nm3, alpha1, beta1, eps1)
        lm4 = h * g(x + km3, y + lm3, z + nm3, alpha2, beta2, eps2)
        nm4 = h * h3(x + km3, y + lm3, z + nm3, delta1, delta2)
        x1 = x + (km1 + 2 * km2 + 2 * km3 + km4)/6
        y1 = y + (lm1 + 2 * lm2 + 2 * lm3 + lm4)/6
        z1 = z + (nm1 + 2 * nm2 + 2 * nm3 + nm4)/6
        xlist.append(x1)
        ylist.append(y1)
        zlist.append(z1)
        x = x1
        y = y1
        z = z1
    return xlist, ylist, zlist


def f(x, y, z, alpha1, beta1, eps1):
    return x * (alpha1 - beta1 * z - x  - eps1 * y)


def g(x, y, z, alpha2, beta2, eps2):
    return y * (alpha2 - beta2 * z - y - eps2 * x)
  
  
def h3(x, y, z, delta1, delta2): 
    return -z * (1 - delta1 * x - delta2 * y + z)


def matlab_export(x_list, y_list, z_list, filename="export.txt"):
    # if os.path.isfile(filename):
        # raise FileExistsError("This file already exists!")
    with open(filename, mode="w") as file:
        for line in map(lambda x, y, z: "{} {} {}".format(x, y, z), x_list, y_list, z_list):
            file.write("{}\n".format(line))

def make_data1(x, y, alpha, delta, h):
    xlist = [x]
    ylist = [y]
    for i in range(100000):
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

def main(alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2, g1):
    m_xp = m_x(alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
    m_yp = m_y(alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
    m_zp = m_z(alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
    x, y, z = make_data(0.9, 0.22, 0, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2)
    x1, y1, z1 = make_data(0.3, 0, 0.2, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2)
    x2, y2, z2 = make_data(0, 0.22, 0.5, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2)
    x3, y3, z3 = make_data(0.9, 0.2, 0.05, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2)
    x4, y4, z4 = make_data(m_xp, m_yp, m_zp, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2)
    # x5, y5, z5 = make_data(0.5, 0.5, -0.5, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2)
    matlab_export(x4, y4, z4, "tr4.txt")
    # matlab_export(x5, y5, z5, "tr5.txt")
    matlab_export(x, y, z, "tr.txt")
    matlab_export(x1, y1, z1, "tr1.txt")
    matlab_export(x2, y2, z2, "tr2.txt")
    matlab_export(x3, y3, z3, "tr3.txt")
    # x2, y2, z2 = make_data(0.65, 0.13, 0, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2, g1)
    # x3, y3, z3 = make_data(1, 1, 1, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2, g1)
    # x1, y1, z1 = make_data(60, 15, alpha, delta)
    # x2, y2, z2 = make_data(110, 10, alpha, delta)

    # x3, y3 = make_data(20, 16, alpha, delta)
    # x4, y4 = make_data(47, 23, alpha, delta)
    # x5, y5 = make_data(2.1, 0.1, alpha, delta)

    # x6, y6 = make_data(50, 23, alpha, delta)
    # sep1, sep2 = make_data1(0, 0.00001, alpha, delta, -0.01)
    # print(x[-1], y[-1], z[-1])
    # fig = pylab.figure()
    # axes = Axes3D(fig)
    # axes.scatter(x, y, z)
    # axes.scatter(x1, y1, z1)
    # axes.scatter(x2, y2, z2)
    # axes.scatter(x3, y3, z3)
    # # plt.plot(x, y)
    # plt.grid(True)
    # plt.xlabel(r'$X$')
    # plt.ylabel(r'$Y$')
    # axes.yaxis._axinfo['linestyle'] = '-'
    # axes.yaxis._axinfo['linewidth'] = 0
    # # plt.zlabel(r'$Z$')
    # pylab.show()


if __name__ == "__main__":
    # main(1.363, 1.147, 1, 5, 5, 1, 0.556, 5, 1)
    main(2.4, 1.758, 4, 10, 6, 1, 0.25, 4, 1)

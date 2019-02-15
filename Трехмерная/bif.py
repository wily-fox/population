import pylab
import math
import os
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from save import *


def make_data(x, y, z, alpha1, alpha2, beta1, beta2, eps1, eps2, delta1, delta2):
    z_bif = (5 * alpha2 - 8) / 10
    h = 0.01
    xlist = []
    ylist = []
    zlist = []
    a2list = [] 
    for i in range(500000):
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
        # if math.fabs(x1 - x) < 0.00001 and math.fabs(y1 - y) < 0.00001 and math.fabs(z1 - z) < 0.00001:
            # xlist.append(x1)
            # ylist.append(y1)
            # zlist.append(z1)
            # a2list.append(alpha2)
            # break
        if x1 > 100 or y1 > 100 or z1 > 100:
            break
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
        # if math.fabs(x1 - x) < 0.00001 and math.fabs(y1 - y) < 0.00001 and math.fabs(z1 - z) < 0.00001:
            # xlist.append(x1)
            # ylist.append(y1)
            # zlist.append(z1)
            # a2list.append(alpha2)
            # break
        if x1 > 100 or y1 > 100 or z1 > 100:
            print("oooops")
            break
        if (z1 - z_bif) * (z - z_bif) < 0:
            xlist.append(x1)
            ylist.append(y1)
            zlist.append(z1)
            a2list.append(alpha2)
        x = x1
        y = y1
        z = z1
    return xlist, ylist, zlist, a2list, x, y, z


def f(x, y, z, alpha1, beta1, eps1):
    return x * (alpha1 - beta1 * z - x  - eps1 * y)


def g(x, y, z, alpha2, beta2, eps2):
    return y * (alpha2 - beta2 * z - y - eps2 * x)
  
  
def h3(x, y, z, delta1, delta2): 
    return -z * (1 - delta1 * x - delta2 * y + z)
    

def m_x(a1, a2, b1, b2, e1, e2, d1, d2):
    return -((a1 + b1 - a2 * b1 * d2 + a1 * b2 * d2 - a2 * e1 - b2 * e1) / (-1 - b1 * d1 - 
        b2 * d2 + b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2))

  
def m_y(a1, a2, b1, b2, e1, e2, d1, d2):
    return -(a2 + b2 + a2 * b1 * d1 - a1 * b2 * d1 - a1 * e2 - b1 * e2)/(-1 - b1 * d1 - b2 * d2 + 
        b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2)
 

def m_z(a1, a2, b1, b2, e1, e2, d1, d2):
    return -((-1 + a1 * d1 + a2 * d2 - a2 * d1 * e1 - a1 * d2 * e2 + e1 * e2)/(-1 - b1 * d1 - 
        b2 * d2 + b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2))
        
        
def main(alpha1, beta1, beta2, eps1, eps2, delta1, delta2):
    i = 1.92727
    x_p = m_x(alpha1, 1.600001, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
    y_p = m_y(alpha1, 1.600001, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
    z_p = m_z(alpha1, 1.600001, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
    allx = []
    ally = []
    allz = []
    alla2 = []
    while i >= 1.6:
        m_xp = m_x(alpha1, i, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
        m_yp = m_y(alpha1, i, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
        m_zp = m_z(alpha1, i, beta1, beta2, eps1, eps2, delta1, delta2) + 0.0001
        x_n, y_n, z_n, a2_n, x_p, y_p, z_p = make_data(m_xp, m_yp, m_zp, alpha1, i, beta1, beta2, eps1, eps2, delta1, delta2)
        allx.extend(x_n)
        ally.extend(y_n)
        # # allz.extend(z_n)
        alla2.extend(a2_n)
        i -= 0.0001
        print(i)
        
    while i >= 0:
        x_n, y_n, z_n, a2_n, x_p, y_p, z_p = make_data(x_p, y_p, z_p, alpha1, i, beta1, beta2, eps1, eps2, delta1, delta2)
        allx.extend(x_n)
        ally.extend(y_n)
        # # allz.extend(z_n)
        alla2.extend(a2_n)
        i -= 0.0001
        print(i)
    # while i <= 1.7538:
        # x_n, y_n, z_n, a2_n, x_p, y_p, z_p = make_data(x_p, y_p, z_p, alpha1, i, beta1, beta2, eps1, eps2, delta1, delta2)
        # # print(x_p, y_p)
        # allx.extend(x_n)
        # ally.extend(y_n)
        # # allz.extend(z_n)
        # alla2.extend(a2_n)
        # i += 0.0000001
        # print(i)
    matlab_export(alla2, allx, "x_bifp.txt")
    matlab_export(alla2, ally, "y_bifp.txt")
    # matlab_export(alla2, allz, "z_bif1.txt")

if __name__ == "__main__":
    # main(1.363, 1.147, 1, 5, 5, 1, 0.556, 5, 1)
    main(2.4, 4, 10, 6, 1, 0.25, 4)
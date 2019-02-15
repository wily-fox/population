from save import *


def b1_x(a1, a2, e1, e2):
    return -((a1 - a2 * e1) / (-1 + e1 * e2))

    
def b1_y(a1, a2, e1, e2):
    return -((a2 - a1 * e2)/(-1 + e1 * e2))

    
def b2_y(a2, b2, d2):
    return -((-a2 - b2)/(1 + b2 * d2))

    
def b2_z(a2, b2, d2):
    return -((1 - a2 * d2)/(1 + b2 * d2))


def m_x(a1, a2, b1, b2, e1, e2, d1, d2):
    return -((a1 + b1 - a2 * b1 * d2 + a1 * b2 * d2 - a2 * e1 - b2 * e1) / (-1 - b1 * d1 - 
  b2 * d2 + b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2))

  
def m_y(a1, a2, b1, b2, e1, e2, d1, d2):
    return -(a2 + b2 + a2 * b1 * d1 - a1 * b2 * d1 - a1 * e2 - b1 * e2)/(-1 - b1 * d1 - b2 * d2 + 
 b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2)
 

def m_z(a1, a2, b1, b2, e1, e2, d1, d2):
    return -((-1 + a1 * d1 + a2 * d2 - a2 * d1 * e1 - a1 * d2 * e2 + e1 * e2)/(-1 - b1 * d1 - 
  b2 * d2 + b2 * d1 * e1 + b1 * d2 * e2 + e1 * e2))




# def make_data(a1, a2, b1, b2, e1, e2, d1, d2, mass, mass_a, i_n, i_p, h, filename):
    # i = i_n
    # while i <= 1.6:
        # mass.append(b1_x(a1, b1, d1))
        # mass_a.append(i)
        # i+=0.001
    # matlab_export(mass_a, mass, "b1_x_n")
    
    
def main(a1, b1, b2, e1, e2, d1, d2):
    i = 0.4
    mass = []
    mass_a = []    
    # while i <= 2.4:
        # mass.append(2.4)
        # mass_a.append(i)
        # i += 0.001
    # matlab_export(mass_a, mass, "a1_x_u.txt")
    # mass.clear()
    # mass_a.clear()
    # while i <= 3:
        # mass.append(2.4)
        # mass_a.append(i)
        # i += 0.001
    # matlab_export(mass_a, mass, "a1_x_n.txt")
    # i = 0.4
    # mass = []
    # mass_a = []
    # while i <= 1.6:
        # mass.append(b1_y(a1, i, e1, e2))
        # mass_a.append(i)
        # i+=0.001
    # matlab_export(mass_a, mass, "b1_y_n.txt")
    # mass.clear()
    # mass_a.clear()
    
    # while i <= 2.4:
        # mass.append(b1_y(a1, i, e1, e2))
        # mass_a.append(i)
        # i += 0.001
    # matlab_export(mass_a, mass, "b1_y_u.txt")
    # mass.clear()
    # mass_a.clear()
    
    i = 1.6
    while i <= 1.7638:
        mass.append(m_y(a1, i, b1, b2, e1, e2, d1, d2))
        mass_a.append(i)
        i += 0.001
    matlab_export(mass_a, mass, "m_y_n.txt")
    mass.clear()
    mass_a.clear()
    
    while i <= 1.92727:
        mass.append(m_y(a1, i, b1, b2, e1, e2, d1, d2))
        mass_a.append(i)
        i += 0.001
    matlab_export(mass_a, mass, "m_y_u.txt")
    mass.clear()
    mass_a.clear()
    
    # i = 0.25
    # while i <= 1.92727:
        # mass.append(b2_z(i, b2, d2))
        # mass_a.append(i)
        # i +=0.001
    # matlab_export(mass_a, mass, "b2_z_n.txt")
    # mass.clear()
    # mass_a.clear()
    
    # while i <= 3:
        # mass.append(b2_z(i, b2, d2))
        # mass_a.append(i)
        # i +=0.001
    # matlab_export(mass_a, mass, "b2_z_u.txt")
        
        
if __name__ == "__main__":
    main(2.4, 4, 10, 6, 1, 0.25, 4)
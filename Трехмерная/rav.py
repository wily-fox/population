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
  
  
def main(a1, a2, b1, b2, e1, e2, d1, d2):
    print("A1: {}, {}, {}".format(a1, 0, 0))
    print("A2: {}, {}, {}".format(0, a2, 0))
    print("B1: {}, {}, {}".format(b1_x(a1, a2, e1, e2), b1_x(a1, a2, e1, e2), 0))
    print("B2: {}, {}, {}".format(0, b2_y(a2, b2, d2), b2_z(a2, b2, d2)))
    print("M: {}, {}, {}".format(m_x(a1, a2, b1, b2, e1, e2, d1, d2), m_y(a1, a2, b1, b2, e1, e2, d1, d2), m_z(a1, a2, b1, b2, e1, e2, d1, d2)))

    
if __name__ == "__main__":
    main(2.4, 0.3, 4, 10, 6, 1, 0.25, 4)    


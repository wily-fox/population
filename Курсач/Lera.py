import pylab
import matplotlib.pyplot as plt

i = 0
list1 = []
delta1 = []
while i <= 0.2999:
    list1.append(2/3)
    delta1.append(i)
    i += 0.0001

i = 0.2999
list2 = []
delta2 = []
while i <= 1:
    list2.append(2/3)
    delta2.append(i)
    i += 0.0001

list3 = []
list4 = []
i = 0
while i <= 1:
    list3.append(1)
    list4.append(i)
    i += 0.1

plt.plot(delta1, list1, 'b', delta2, list2, 'r', list4, list3, 'r', list4, list4, 'b')
plt.grid(True)
plt.axis([0, 1, 0, 1.5])
pylab.show()

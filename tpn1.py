import numpy as np
import math
import matplotlib.pyplot as plt
import signals as sig
import operaciones as op
import interpolador as inter
import ruido as ns

tiempo, senal = sig.seno(0, 1, 2, 100, 1, 0)
tiempo2, senal2 = sig.seno(0, 1, 4, 100, 1, 0)


def suma(s1, s2):
    sum = []
    for i in range(len(s1)):
        sum.append(s1[i]+s2[i])
    return sum


# tiempo2, senal2 = inter.intersinc(senal, 100, 2000, -1, 1)
# tiempo, senal = sig.sinc(0, 1, 5, 1000, 1, 0)
sum = suma(senal, senal2)

plt.grid()
plt.plot(tiempo, senal)
plt.plot(tiempo2, senal2)
plt.plot(tiempo, sum)
plt.show()

import numpy as np
import math
import matplotlib.pyplot as plt
import signals as sig
import operaciones as op
import interpolador as inter

tiempo, senal = sig.seno(0, 1, 2, 100, 1, 0)
tiempo2, senal2 = inter.intersinc(senal, 100, 2000, 0, 1)
# tiempo, senal = sig.sinc(0, 1, 5, 1000, 1, 0)
plt.grid()
plt.plot(tiempo, senal)
plt.plot(tiempo2, senal2)
plt.show()

import numpy as np
import math
import matplotlib.pyplot as plt
import signals as sgl
import operaciones as op


def lineal(t):
    if abs(t) < 1:
        return 1-abs(t)
    else:
        return 0


def interlineal(s, fo, fn, ti, tf):
    T = 1/fo
    Ti = 1/fn
    n = len(s)
    m = (n-1)*(fn/fo)+1
    sig = []
    acum = 0
    tiempo = np.arange(ti, tf, (tf-ti)/m)
    for i in range(int(m)):
        acum = 0
        for j in range(n):
            acum += s[j]*lineal((i*Ti-j*T)/T)
        sig.append(acum)

    return tiempo, sig


def nearest(array, value):
    return np.argmin(np.abs(array-value))


def intersinc(s, fo, fn, ti, tf):
    T = 1/fo
    Ti = 1/fn
    n = len(s)
    m = (n-1)*(fn/fo)+1
    sig = []
    acum = 0
    tiempo = np.arange(ti, tf, (tf-ti)/m)
    for i in range(int(m)):
        acum = 0
        for j in range(n):
            argumento = (i*Ti-j*T)/T
            acum += s[j]*np.sinc(argumento)
        sig.append(acum)
    return tiempo, sig

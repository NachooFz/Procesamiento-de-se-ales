
import numpy as np
import math


def c(tin, tfin, fs, fm, amp, fase):
    T = 1/fm
    tiempo = np.arange(tin, tfin, T)
    senoidal = []
    for t in tiempo:
        if np.mod(2*math.pi*fs*t + fase, 2*math.pi) >= math.pi:
            senoidal.append(-1)
        else:
            senoidal.append(1)
    return tiempo, senoidal


def sinc(tin, tfin, fs, fm, amp, fase):
    T = 1/fm
    tiempo = np.arange(tin, tfin, T)
    senoidal = []
    for t in tiempo:
        x = 2*math.pi*fs*t + fase
        senoidal.append(amp*np.sinc(x))
    return tiempo, senoidal


def seno(tin, tfin, fm, fa, amp, fase):
    T = 1/fa
    tiempo = np.arange(tin, tfin, T)
    senoidal = []
    for t in tiempo:
        senoidal.append(amp*math.sin(2*math.pi*fm*t + fase))
    return tiempo, senoidal

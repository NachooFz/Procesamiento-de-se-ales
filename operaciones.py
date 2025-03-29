import numpy as np
import math


def positivizar(s):
    minimo = min(s)
    positiva = []
    for i in s:
        positiva.append(i-minimo)
    return positiva


def cuantificador(s, n):
    minimo = min(s)
    senal = positivizar(s)
    cuantificada = []
    final = []
    h = (max(senal) - min(senal))/n
    for i in senal:
        if i < 0:
            i = 0
        elif 0 <= i < h*(n-1):
            i = h*int(i/h)
        elif i >= h*(n-1):
            i = h*(n-1)
        cuantificada.append(i+minimo+h/2)

    return cuantificada

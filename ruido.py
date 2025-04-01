import numpy as np
import math
import matplotlib.pyplot as plt
import sounddevice as sd
import signals as sig
import operaciones as op


def noise_sig(tin, tfin, fs=1000, amp=1):
    T = 1/fs
    tiempo = np.arange(tin, tfin, T)
    ruido = np.random.rand(len(tiempo))
    return tiempo, ruido


def pot_sig(s):
    potencia = 0
    for i in range(len(s)):
        potencia += s[i]**2
    return potencia/len(s)


def snr(s, ruido):
    potencia_senal = pot_sig(senal)
    potencia_ruido = pot_sig(ruido)
    return 10*math.log10(potencia_senal/potencia_ruido)


tiempo, ruido = noise_sig(0, 1, 1000, 1)
tiempo2, senal = sig.seno(0, 1, 5, 1000, 1, 0)

alpha = 3

alpha = math.sqrt(pot_sig(senal)/pot_sig(ruido))
ruido = ruido*alpha
senalruido = senal+ruido
print("SNR: ", snr(senal, ruido))

plt.plot(tiempo, senalruido)
plt.show()
plt.title("Ruido")

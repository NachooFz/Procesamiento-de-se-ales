import numpy as np
import math
import matplotlib.pyplot as plt
import signals as sig


def cal_potencia(senal):
    acum = 0
    for s in senal:
        acum += s*s
    return acum/len(senal)


def cal_SNR(senal, ruido):
    return 10*math.log10(cal_potencia(senal)/cal_potencia(ruido))


tiempo, senal = sig.seno(0, 1, 2, 100, 1, 0)
ruido = np.random.rand(len(tiempo))
senal_final = senal+ruido
print('SNR con ruido que varia entre 0 y 1 : {}'.format(cal_SNR(senal, ruido)))


plt.grid()
plt.plot(tiempo, senal)
plt.plot(tiempo, ruido)
plt.plot(tiempo, senal_final)
plt.show()

# señal ruido multiplicada una constante
alpha = 3
ruido = ruido*alpha
print('SNR con ruido que varia entre 0 y 1  (multiplicado alpha={}) : {}'.format(
    alpha, cal_SNR(senal, ruido)))


# luego del despeje llegamos a que alpha= raiz(Ps/Pr)
alpha = math.sqrt(cal_potencia(senal)/cal_potencia(ruido))
ruido = ruido*alpha
print('Luego de despejar alpha =raiz(Ps/Pr) con ruido que varia entre 0 y 1  (multiplicado alpha={}) : {}'.format(alpha, cal_SNR(senal, ruido)))
print('observamos que SNR aproximadamente 0')
plt.grid()
plt.plot(tiempo, senal)
plt.plot(tiempo, ruido)
plt.plot(tiempo, senal_final)
plt.show()

# Indicar qual a temperatura máxima e qual a temperatura mínima.


def minMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "ºC.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "ºC.")


def minima(t):
    min = t[0]
    for i in range(len(t)):
        if t[i] < min:
            min = t[i]
    return min


def maxima(t):
    max = t[0]
    for i in range(len(t)):
        if t[i] > max:
            max = t[i]
    return max

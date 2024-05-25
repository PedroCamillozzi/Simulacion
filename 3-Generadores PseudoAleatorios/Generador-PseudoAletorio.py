import random as rnd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm


class GLC:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m
#       seed=> semilla inicial, a=> multiplicador, c=> incremento constante, m=> módulo

    def random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / self.m


class MidSquareRNG:
    def __init__(self, seed, n_digits):
        self.seed = seed
        self.n_digits = n_digits

    def random(self):
        # Elevar al cuadrado el número semilla
        squared = self.seed ** 2

        # Convertir a string para facilitar la extracción de los dígitos centrales
        squared_str = str(squared).zfill(2 * self.n_digits)

        # Calcular el número de dígitos a eliminar en cada lado
        start = (len(squared_str) - self.n_digits) // 2
        end = start + self.n_digits

        # Extraer los dígitos centrales
        new_seed_str = squared_str[start:end]

        # Convertir los dígitos centrales de vuelta a un número entero
        self.seed = int(new_seed_str)

        return self.seed


def main():
    glcresults = []
    msmresults = []
    randomlibraryresults = []
    seed = 42
    a = 1664525
    c = 1013904223
    m = 2 ** 32

    generatorglc = GLC(seed, a, c, m)

    print('GLC')
    for i in range(5000):
        glcresults.append(generatorglc.random())
        print(glcresults[i])

    print('random library, seed setted = ', seed)
    rnd.seed(seed)
    for i in range(5000):
        randomlibraryresults.append(rnd.random())
        print(randomlibraryresults[i])

    print('Mid-Square')
    seed = 1382
    generatormsm = MidSquareRNG(seed, n_digits=4)
    for i in range(5000):
        nrorandom = generatormsm.random()
        msmresults.append(nrorandom**2/100000000)
        print('Semilla: ', nrorandom, 'Valor: ', msmresults[i])
        if msmresults[i] == 0:
            break

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    x1 = randomlibraryresults
    y1 = np.linspace(0, 1, len(randomlibraryresults))
    h1 = ax1.hist2d(x1, y1, bins=40, norm=LogNorm())
    fig.colorbar(h1[3], ax=ax1)
    ax1.set_title('Histograma Random Library')

    x2 = msmresults
    y2 = np.linspace(0, 1, len(msmresults))
    h2 = ax2.hist2d(x2, y2, bins=40, norm=LogNorm())
    fig.colorbar(h2[3], ax=ax2)
    ax2.set_title('Histograma Mid-Square')

    plt.tight_layout()
    plt.savefig('RandomLibraryvsMid-Square.png')
    plt.show()


if __name__ == "__main__":
    main()
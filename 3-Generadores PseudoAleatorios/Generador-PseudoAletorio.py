import random as rnd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
from scipy.stats import chi2


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


class MersenneTwister:
    def __init__(self, seed):
        self.mt = [0] * 624
        self.index = 0
        self.mt[0] = seed
        for i in range(1, 624):
            self.mt[i] = (0x6c078965 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i) & 0xffffffff

    def extract_number(self):
        if self.index == 0:
            self._twist()

        y = self.mt[self.index]
        y = y ^ (y >> 11)
        y = y ^ ((y << 7) & 0x9d2c5680)
        y = y ^ ((y << 15) & 0xefc60000)
        y = y ^ (y >> 18)

        self.index = (self.index + 1) % 624
        return y / 0xffffffff

    def _twist(self):
        for i in range(624):
            y = (self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)
            self.mt[i] = self.mt[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908b0df

def chi_square_test(observed, expected):
    chi_squared = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    degrees_of_freedom = len(observed) - 1
    p_value = 1 - chi2.cdf(chi_squared, degrees_of_freedom)
    return chi_squared, p_value


def waiting_time_test(sequence, subinterval):
    count = sum(1 for num in sequence if subinterval[0] <= num < subinterval[1])
    prob_subinterval = count / len(sequence)
    waiting_times = []
    last_index = -1
    for i, num in enumerate(sequence):
        if subinterval[0] <= num < subinterval[1]:
            if last_index != -1:
                waiting_times.append(i - last_index - 1)
            last_index = i
    p = 1 - prob_subinterval
    expected_waiting_times = [1 / p] * len(waiting_times)
    chi_squared, p_value = chi_square_test(waiting_times, expected_waiting_times)
    return chi_squared, p_value


def main():
    glcresults = []
    mtresults = []
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

    print('Mersenne Twister, seed setted = ', seed)
    generatormt = MersenneTwister(seed)
    for i in range(5000):
        mtresults.append(generatormt.extract_number())
        print(mtresults[i])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    op = int(input("1- GLC vs MT 2- GLC vs Random Lirary 3- MT vs Random Lirary: "))
    y1 = np.linspace(0, 1, len(randomlibraryresults))
    y2 = np.linspace(0, 1, len(mtresults))

    if op == 1:
        x1 = glcresults
        x2 = mtresults
        h1 = ax1.hist2d(x1, y1, bins=40, norm=LogNorm())
        fig.colorbar(h1[3], ax=ax1)
        h2 = ax2.hist2d(x2, y2, bins=40, norm=LogNorm())
        ax1.set_title('Histograma GLC')
        fig.colorbar(h2[3], ax=ax2)
        ax2.set_title('Histograma Mesrsenne Twister')
    elif op == 2:
        x1 = glcresults
        x2 = randomlibraryresults
        h1 = ax1.hist2d(x1, y1, bins=40, norm=LogNorm())
        fig.colorbar(h1[3], ax=ax1)
        h2 = ax2.hist2d(x2, y2, bins=40, norm=LogNorm())
        ax1.set_title('Histograma GLC')
        fig.colorbar(h2[3], ax=ax2)
        ax2.set_title('Histograma Random Lirary')
    elif op == 3:
        x1 = mtresults
        x2 = randomlibraryresults
        h1 = ax1.hist2d(x1, y1, bins=40, norm=LogNorm())
        fig.colorbar(h1[3], ax=ax1)
        h2 = ax2.hist2d(x2, y2, bins=40, norm=LogNorm())
        ax2.set_title('Histograma Mersenne Twister')
        fig.colorbar(h2[3], ax=ax2)
        ax2.set_title('Histograma Random Lirary')

    plt.tight_layout()
#    plt.savefig('GLCvsMT.png')
    plt.show()

    # Pruebas estadísticas
    print("\nPruebas estadísticas GLC:")
    # Prueba de bondad de ajuste (Chi-cuadrado)
    print("\nPrueba de bondad de ajuste (Chi-cuadrado):")
    expected_freq = [len(glcresults) / 10] * 10  # 10 bins
    observed_freq, _ = np.histogram(glcresults, bins=10)
    chi_squared, p_value = chi_square_test(observed_freq, expected_freq)
    print("Chi-cuadrado:", chi_squared)
    print("P-valor:", p_value)
    # Prueba de espera
    print("\nPrueba de espera:")
    chi_squared, p_value = waiting_time_test(glcresults, (0.4, 0.6))
    print("Chi-cuadrado:", chi_squared)
    print("P-valor:", p_value)

    print("\nPruebas estadísticas RANDOM LIBRARY:")
    # Prueba de bondad de ajuste (Chi-cuadrado)
    print("\nPrueba de bondad de ajuste (Chi-cuadrado):")
    expected_freq = [len(randomlibraryresults) / 10] * 10  # 10 bins
    observed_freq, _ = np.histogram(randomlibraryresults, bins=10)
    chi_squared, p_value = chi_square_test(observed_freq, expected_freq)
    print("Chi-cuadrado:", chi_squared)
    print("P-valor:", p_value)
    # Prueba de espera
    print("\nPrueba de espera:")
    chi_squared, p_value = waiting_time_test(randomlibraryresults, (0.4, 0.6))
    print("Chi-cuadrado:", chi_squared)
    print("P-valor:", p_value)

    print("\nPruebas estadísticas Mersenne Twister:")
    # Prueba de bondad de ajuste (Chi-cuadrado)
    print("\nPrueba de bondad de ajuste (Chi-cuadrado):")
    expected_freq = [len(mtresults) / 10] * 10  # 10 bins
    observed_freq, _ = np.histogram(mtresults, bins=10)
    chi_squared, p_value = chi_square_test(observed_freq, expected_freq)
    print("Chi-cuadrado:", chi_squared)
    print("P-valor:", p_value)
    print("\nPruebas estadísticas Mersenne Twister:")
    # Prueba de espera
    print("\nPrueba de espera:")
    chi_squared, p_value = waiting_time_test(mtresults, (0.4, 0.6))
    print("Chi-cuadrado:", chi_squared)
    print("P-valor:", p_value)


if __name__ == "__main__":
    main()

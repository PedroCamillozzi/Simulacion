import random as rnd
import matplotlib.pyplot as plt
import math


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


def exponential_transform(u, lambd):
    return -math.log(1 - u) / lambd


def gamma_transform(u_list, beta):
    return sum(-math.log(1 - u) / beta for u in u_list)


def normal_transform(u1, u2):
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    z1 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)
    return z0, z1


def pascal_transform(u_list, r, p):
    n = 0
    successes = 0
    while successes < r:
        if not u_list:
            raise ValueError("Lista de números aleatorios agotada")
        if u_list.pop(0) < p:
            successes += 1
        n += 1
    return n


def binomial_transform(u_list, n, p):
    successes = 0
    for _ in range(n):
        if not u_list:
            raise ValueError("Lista de números aleatorios agotada")
        if u_list.pop(0) < p:
            successes += 1
    return successes


def hypergeometric_transform(u_list, N, K, n):
    good_elements = 0
    for _ in range(n):
        if not u_list:
            raise ValueError("Lista de números aleatorios agotada")
        if u_list.pop(0) < K / N:
            good_elements += 1
            K -= 1
        N -= 1
    return good_elements


def poisson_transform(u_list, lambd):
    n = 0
    p = math.exp(-lambd)
    F = p
    while True:
        if not u_list:
            raise ValueError("Lista de números aleatorios agotada")
        if u_list.pop(0) < F:
            return n
        n += 1
        p *= lambd / n
        F += p


def empirical_discrete_transform(u_list, probabilities):
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    for i, cumulative_prob in enumerate(cumulative_probabilities):
        if not u_list:
            raise ValueError("Lista de números aleatorios agotada")
        if u_list[0] < cumulative_prob:
            return i
    raise ValueError("No se pudo generar un valor con la distribución de probabilidad empírica discreta")


def main():
    glcresults = []
    mtresults = []
    randomlibraryresults = []

    lambd = 1
    alpha = 2
    beta = 1

    seed = 42
    a = 1664525
    c = 1013904223
    m = 2 ** 32



    op = int(input("Seleccione el tipo de Distribución: 1-Uniforme 2-Exponencial 3-Gamma 4-Normal 5-Pascal 6-Binomial 7-Hipergeométrica 8- Poisson 9-Empírica Discreta: "))

    generatorglc = GLC(seed, a, c, m)

    print('GLC')
    resultaux = None
    for i in range(5000):
        result = generatorglc.random()
        if op == 1:
            glcresults.append(result)
            print(glcresults[i])
        elif op == 2:
            glcresults.append(exponential_transform(result, lambd))
            print(glcresults[i])
        elif op == 3:
            listaux = [generatorglc.random() for _ in range(alpha)]
            glcresults.append(gamma_transform(listaux, beta))
            print(glcresults[i])
        elif op == 4:
            if resultaux is None:
                resultaux = result
            else:
                z0, z1 = normal_transform(resultaux, result)
                glcresults.extend([z0, z1])
                resultaux = None
                print(glcresults[i-1])
                print(glcresults[i])
        elif op == 5:
            p = 0.5
            r = 5
            listaux = [generatorglc.random() for _ in range(10)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                pascal_result = pascal_transform(listaux, r, p)
                glcresults.append(pascal_result)
                print(glcresults[-1])
            except ValueError as e:
                print("")
        elif op == 6:
            n = 10
            p = 0.5
            listaux = [generatorglc.random() for _ in range(n)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                binomial_result = binomial_transform(listaux, n, p)
                glcresults.append(binomial_result)
                print(glcresults[-1])
            except ValueError as e:
                print("")
        elif op == 7:
            N = 100  # Tamaño de la población
            K = 20  # Número de elementos aen la población con la característica de interés
            n = 10  # Tamaño de la muestr
            listaux = [generatorglc.random() for _ in range(N)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                hypergeometric_result = hypergeometric_transform(listaux, N, K, n)
                glcresults.append(hypergeometric_result)
                print(glcresults[-1])
            except ValueError as e:
                print("")
        elif op == 8:
            listaux = [generatorglc.random() for _ in
                       range(10)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                poisson_result = poisson_transform(listaux, lambd)
                glcresults.append(poisson_result)
                print(glcresults[-1])
            except ValueError as e:
                print("")
        elif op == 9:
            probabilities = [0.2, 0.3, 0.1, 0.25, 0.15]
            listaux = [generatorglc.random() for _ in range(len(probabilities))]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                empirical_discrete_result = empirical_discrete_transform(listaux, probabilities)
                glcresults.append(empirical_discrete_result)
                print(glcresults[-1])
            except ValueError as e:
                print("")

    print('random library, seed setted = ', seed)
    rnd.seed(seed)
    resultaux = None
    for i in range(5000):
        result = rnd.random()
        if op == 1:
            randomlibraryresults.append(result)
            print(randomlibraryresults[i])
        elif op == 2:
            randomlibraryresults.append(exponential_transform(result, lambd))
            print(randomlibraryresults[i])
        elif op == 3:
            listaux = [rnd.random() for _ in range(alpha)]
            randomlibraryresults.append(gamma_transform(listaux, beta))
            print(randomlibraryresults[i])
        elif op == 4:
            if resultaux is None:
                resultaux = result
            else:
                z0, z1 = normal_transform(resultaux, result)
                randomlibraryresults.extend([z0, z1])
                resultaux = None
                print(randomlibraryresults[i-1])
                print(randomlibraryresults[i])
        elif op == 5:
            p = 0.5
            r = 5
            listaux = [rnd.random() for _ in range(10)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                pascal_result = pascal_transform(listaux, r, p)
                randomlibraryresults.append(pascal_result)
                print(randomlibraryresults[-1])
            except ValueError as e:
                print("")
        elif op == 6:
            n = 10
            p = 0.5
            listaux = [rnd.random() for _ in range(n)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                binomial_result = binomial_transform(listaux, n, p)
                randomlibraryresults.append(binomial_result)
                print(randomlibraryresults[-1])
            except ValueError as e:
                print("")
        elif op == 7:
            N = 100  # Tamaño de la población
            K = 20  # Número de elementos en la población con la característica de interés
            n = 10  # Tamaño de la muestra
            listaux = [rnd.random() for _ in range(N)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                hypergeometric_result = hypergeometric_transform(listaux, N, K, n)
                randomlibraryresults.append(hypergeometric_result)
                print(randomlibraryresults[-1])
            except ValueError as e:
                print("")
        elif op == 8:
            listaux = [rnd.random() for _ in
                       range(10)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                poisson_result = poisson_transform(listaux, lambd)
                randomlibraryresults.append(poisson_result)
                print(randomlibraryresults[-1])
            except ValueError as e:
                print("")
        elif op == 9:
            probabilities = [0.2, 0.3, 0.1, 0.25, 0.15]
            listaux = [rnd.random() for _ in range(len(probabilities))]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                empirical_discrete_result = empirical_discrete_transform(listaux, probabilities)
                randomlibraryresults.append(empirical_discrete_result)
                print(randomlibraryresults[-1])
            except ValueError as e:
                print("")


    print('Mersenne Twister, seed setted = ', seed)
    generatormt = MersenneTwister(seed)
    resultaux = None
    for i in range(5000):
        result = generatormt.extract_number()
        if op == 1:
            mtresults.append(result)
            print(mtresults[i])
        elif op == 2:
            mtresults.append(exponential_transform(result, lambd))
            print(mtresults[i])
        elif op == 3:
            listaux = [generatormt.extract_number() for _ in range(alpha)]
            mtresults.append(gamma_transform(listaux, beta))
            print(mtresults[i])
        elif op == 4:
            if resultaux is None:
                resultaux = result
            else:
                z0, z1 = normal_transform(resultaux, result)
                mtresults.extend([z0, z1])
                resultaux = None
                print(mtresults[i-1])
                print(mtresults[i])
        elif op == 5:
            p = 0.5
            r = 5
            listaux = [generatormt.extract_number() for _ in range(10)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                pascal_result = pascal_transform(listaux, r, p)
                mtresults.append(pascal_result)
                print(mtresults[-1])
            except ValueError as e:
                print("")
        elif op == 6:
            n = 10
            p = 0.5
            listaux = [generatormt.extract_number()  for _ in range(n)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                binomial_result = binomial_transform(listaux, n, p)
                mtresults.append(binomial_result)
                print(mtresults[-1])
            except ValueError as e:
                print("")
        elif op == 7:
            N = 100  # Tamaño de la población
            K = 20  # Número de elementos en la población con la característica de interés
            n = 10  # Tamaño de la muestra
            listaux = [generatormt.extract_number() for _ in range(N)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                hypergeometric_result = hypergeometric_transform(listaux, N, K, n)
                mtresults.append(hypergeometric_result)
                print(mtresults[-1])
            except ValueError as e:
                print("")
        elif op == 8:
            listaux = [generatormt.extract_number() for _ in
                       range(10)]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                poisson_result = poisson_transform(listaux, lambd)
                mtresults.append(poisson_result)
                print(mtresults[-1])
            except ValueError as e:
                print("")
        elif op == 9:
            probabilities = [0.2, 0.3, 0.1, 0.25, 0.15]
            listaux = [generatormt.extract_number() for _ in range(len(probabilities))]  # Genera una lista de números aleatorios uniformemente distribuidos
            try:
                empirical_discrete_result = empirical_discrete_transform(listaux, probabilities)
                mtresults.append(empirical_discrete_result)
                print(mtresults[-1])
            except ValueError as e:
                print("")

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.hist(glcresults, bins=50, color='blue', alpha=0.7)
    plt.title('GLC')

    plt.subplot(1, 3, 2)
    plt.hist(mtresults, bins=50, color='green', alpha=0.7)
    plt.title('Mersenne Twister')

    plt.subplot(1, 3, 3)
    plt.hist(randomlibraryresults, bins=50, color='red', alpha=0.7)
    plt.title('Random Library')

    plt.suptitle('Distribución Empírica Discreta de Números Pseudoaleatorios')
    plt.savefig('Distribución de Probabilidad Empírica Discreta')
    plt.show()


if __name__ == "__main__":
    main()

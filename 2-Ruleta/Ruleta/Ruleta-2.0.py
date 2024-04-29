import random
import matplotlib.pyplot as plt
import numpy as np


def girar_ruleta():
    return random.randint(0, 36)


def simulacion(tiradas, numero_elegido):
    resultados = []
    for _ in range(tiradas):
        resultados.append(girar_ruleta())

    frecuencia_numero_elegido = resultados.count(numero_elegido)
    probabilidad = frecuencia_numero_elegido / tiradas
    frecuencia_relativa = frecuencia_numero_elegido / len(resultados)
    valor_promedio = np.mean(resultados)
    desvio = np.std(resultados)
    varianza = np.var(resultados)

    return resultados, probabilidad, frecuencia_relativa, valor_promedio, desvio, varianza


def main():
    tiradas = int(input("Ingrese la cantidad de tiradas: "))
    corridas = int(input("Ingrese la cantidad de corridas: "))
    numero_elegido = int(input("Ingrese el número elegido (0-36): "))

    resultados = []
    probabilidades = []
    frecuencias_relativas = []
    valores_promedio = []
    desvios = []
    varianzas = []
    for _ in range(corridas):
        resultado, probabilidad, frecuencia_relativa, valor_promedio, desvio, varianza = simulacion(tiradas,

                                                                                                    numero_elegido)
        probabilidades.append(probabilidad)
        frecuencias_relativas.append(frecuencia_relativa)
        valores_promedio.append(valor_promedio)
        desvios.append(desvio)
        varianzas.append(varianza)
        resultados.extend(resultado)

    tiradas_y_corridas = list(range(corridas*tiradas))

    fig, ax = plt.subplots(figsize=(20, 8))
    ax.scatter(tiradas_y_corridas, resultados)
    ax.legend()
    plt.show()
    
    print("Frecuencia relativa del número elegido:", np.mean(frecuencias_relativas))
    print("Valor promedio total:", np.mean(valores_promedio))
    print("Desvío:", np.mean(desvios))
    print("Varianza:", np.mean(varianzas))


if __name__ == "__main__":
    main()

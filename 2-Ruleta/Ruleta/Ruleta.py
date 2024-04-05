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

    probabilidades = []
    frecuencias_relativas = []
    valores_promedio = []
    desvios = []
    varianzas = []
    for _ in range(corridas):
        resultados, probabilidad, frecuencia_relativa, valor_promedio, desvio, varianza = simulacion(tiradas,
                                                                                                     numero_elegido)
        probabilidades.append(probabilidad)
        frecuencias_relativas.append(frecuencia_relativa)
        valores_promedio.append(valor_promedio)
        desvios.append(desvio)
        varianzas.append(varianza)
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.hist(frecuencias_relativas, bins=10, color='blue', edgecolor='black', alpha=0.7)
    plt.title('Frecuencia Relativa')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')

    plt.subplot(2, 2, 2)
    plt.hist(valores_promedio, bins=10, color='green', edgecolor='black', alpha=0.7)
    plt.title('Valor Promedio')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')

    plt.subplot(2, 2, 3)
    plt.hist(desvios, bins=10, color='red', edgecolor='black', alpha=0.7)
    plt.title('Desvío')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')

    plt.subplot(2, 2, 4)
    plt.hist(varianzas, bins=10, color='orange', edgecolor='black', alpha=0.7)
    plt.title('Varianza')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')

    plt.tight_layout()
    plt.savefig('Gráficas-Ruleta-2.png')
    plt.show()

    print("Frecuencia relativa del número elegido:", np.mean(frecuencias_relativas))
    print("Valor promedio total:", np.mean(valores_promedio))
    print("Desvío:", np.mean(desvios))
    print("Varianza:", np.mean(varianzas))


if __name__ == "__main__":
    main()








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

#   Promedio, Varianza y Desvio por observacion
    promedio_por_observacion = []
    varianza_por_observacion = []
    desvio_por_observacion = []
    aux_resultados = []
    for i in range(resultados.__len__()):
        aux_resultados.append(resultados[i])
        varianza_por_observacion.append(np.var(aux_resultados))
        desvio_por_observacion.append(np.std(aux_resultados))
        promedio_por_observacion.append(np.mean(aux_resultados))

#   Promedio, Varianza y Desvio del numero elegido
    frecuencia_relavtiva_nro_elegido = []
    promedio_nro_elegido = []
    varianza_nro_elegido = []
    desvio_nro_elegido = []
    aux_resultados = []
    aux_resultado_elegido = []
    for i in range(resultados.__len__()):
        aux_resultados.append(resultados[i])
        if resultados[i] == numero_elegido:
            aux_resultado_elegido.append(resultados[i])
        frecuencia_relavtiva_nro_elegido.append(len(aux_resultado_elegido) / len(aux_resultados))
        if len(aux_resultado_elegido) > 0:
            varianza_nro_elegido.append(np.var(frecuencia_relavtiva_nro_elegido))
            desvio_nro_elegido.append(np.std(frecuencia_relavtiva_nro_elegido))
            promedio_nro_elegido.append(np.mean(frecuencia_relavtiva_nro_elegido))
        else:
            varianza_nro_elegido.append(0.0)
            desvio_nro_elegido.append(0.0)
            promedio_nro_elegido.append(0.0)


#   Graficas
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.set_title("Dispersión de los valores de la muestra")
    ax.set_xlabel("Valor")
    ax.set_ylabel("Repeticiones")
    ax.scatter(tiradas_y_corridas, resultados)

    fig, ax2 = plt.subplots(figsize=(20, 8))
    ax2.set_title("Promedio de los valores por cada observación")
    ax2.set_xlabel("Valor")
    ax2.set_ylabel("Repeticiones")
    ax2.plot(tiradas_y_corridas, promedio_por_observacion)
    ax2.axhline(y=18, color='r', linestyle='--')

    fig, ax3 = plt.subplots(figsize=(20, 8))
    ax3.set_title("Varianza de los valores en cada observación")
    ax3.set_xlabel("Valor")
    ax3.set_ylabel("Repeticiones")
    ax3.plot(tiradas_y_corridas, varianza_por_observacion)
    ax3.axhline(y=18, color='r', linestyle='--')

#   Hacer grafica del desvío
    fig, ax4 = plt.subplots(figsize=(20, 8))
    ax4.set_title("Desvio de valores en cada observacion")
    ax4.set_xlabel("Valor")
    ax4.set_ylabel("Repeticiones")
    ax4.plot(tiradas_y_corridas, desvio_por_observacion)

#   Hacer gráfica de frecuencia relativa respecto a un numero que yo elija del 0 al 36
    fig, ax5 = plt.subplots(figsize=(20, 8))
    ax5.set_title("Frecuencia relativa del número " + numero_elegido.__str__())
    ax5.set_xlabel("Valor")
    ax5.set_ylabel("Repeticiones")
    ax5.axhline(y=1/37, color='r', linestyle='--')
    ax5.plot(tiradas_y_corridas, frecuencia_relavtiva_nro_elegido)

#   Hacer gráfica de la varianza frecuencia relativa respecto a un numero que yo elija del 0 al 36
    fig, ax6 = plt.subplots(figsize=(20, 8))
    ax6.set_title("Varianza de la frecuencia relativa del número " + numero_elegido.__str__())
    ax6.set_xlabel("Valor")
    ax6.set_ylabel("Repeticiones")
    ax6.plot(tiradas_y_corridas, varianza_nro_elegido)

#   Hacer gráfica del desvio frecuencia relativa respecto a un numero que yo elija del 0 al 36
    fig, ax7 = plt.subplots(figsize=(20, 8))
    ax7.set_title("Desvio de la frecuencia relativa del número " + numero_elegido.__str__())
    ax7.set_xlabel("Valor")
    ax7.set_ylabel("Repeticiones")
    ax7.plot(tiradas_y_corridas, desvio_nro_elegido)

#   Hacer gráfica del promedio respecto a un número que yo elija del 0 al 36
    fig, ax8 = plt.subplots(figsize=(20, 8))
    ax8.set_title("Promedio de la frecuencia relativa del número " + numero_elegido.__str__())
    ax8.set_xlabel("Valor")
    ax8.set_ylabel("Repeticiones")
    ax8.axhline(y=1/37, color='r', linestyle='--')
    ax8.plot(tiradas_y_corridas, promedio_nro_elegido)

    plt.show()

    print("Frecuencia relativa del número elegido:", np.mean(frecuencias_relativas))
    print("Valor promedio total:", np.mean(valores_promedio))
    print("Desvío:", np.mean(desvios))
    print("Varianza:", np.mean(varianzas))
    print("varianza nro elegido:", varianza_nro_elegido)
    print("Desvio nro elegido: ", desvio_nro_elegido)


if __name__ == "__main__":
    main()

import random
import matplotlib.pyplot as plt
import sys


def girar_ruleta():
    return random.randint(0, 36)


def simulacion(tiradas):
    resultados = []
    for _ in range(tiradas):
        resultados.append(girar_ruleta())

    return resultados


def martingala(resultados, numeros_elegidos, dinero_a_apostar):
    dinamica_dinero = []
    dinero_en_juego = 1
    for i in range(resultados.__len__()):
        if dinero_a_apostar > dinero_en_juego:
            if resultados[i] in numeros_elegidos:
                dinero_a_apostar += dinero_en_juego
                dinamica_dinero.append(dinero_a_apostar)
                dinero_en_juego = 1
            else:
                dinero_a_apostar -= dinero_en_juego
                dinamica_dinero.append(dinero_a_apostar)
                dinero_en_juego *= 2
        else:
            dinamica_dinero.append(0.0)
    if dinamica_dinero[dinamica_dinero.__len__() - 1] == 0:
        print('Banca Rota :(')

    return dinamica_dinero


def dalambert(resultados, numeros_elegidos, dinero_a_apostar):
    dinamica_dinero = []
    dinero_en_juego = 1
    for i in range(resultados.__len__()):
        if dinero_a_apostar > dinero_en_juego:
            if resultados[i] in numeros_elegidos:
                dinero_a_apostar += dinero_en_juego
                dinamica_dinero.append(dinero_a_apostar)
                if dinero_en_juego == 1:
                    dinero_en_juego = 1
                else:
                    dinero_en_juego -= 1
            else:
                dinero_a_apostar -= dinero_en_juego
                dinamica_dinero.append(dinero_a_apostar)
                dinero_en_juego += 1
        else:
            dinamica_dinero.append(0.0)
    if dinamica_dinero[dinamica_dinero.__len__() - 1] == 0:
        print('Banca Rota :(')

    return dinamica_dinero


def fibonacci(resultados, numeros_elegidos, dinero_a_apostar):
    dinamica_dinero = []
    dinero_en_juego = secuenciafibonacci(dinero_a_apostar)
    contador = 1
    for i in range(resultados.__len__()):
        if dinero_a_apostar > dinero_en_juego[contador]:
            if resultados[i] in numeros_elegidos:
                dinero_a_apostar += dinero_en_juego[contador]
                dinamica_dinero.append(dinero_a_apostar)
                if contador < 3:
                    contador = 1
                else:
                    contador -= 2
            else:
                dinero_a_apostar -= dinero_en_juego[contador]
                dinamica_dinero.append(dinero_a_apostar)
                contador += 1
        else:
            dinamica_dinero.append(0.0)
    if dinamica_dinero[dinamica_dinero.__len__() - 1] == 0:
        print('Banca Rota :(')

    return dinamica_dinero


def secuenciafibonacci(dinero_a_apostar):
    secuencia = [0, 1]
    for i in range(2, dinero_a_apostar):
        resultado = secuencia[-1] + secuencia[-2]
        secuencia.append(resultado)

    return secuencia


def paroli(resultados, numeros_elegidos, dinero_a_apostar):
    dinamica_dinero = []
    dinero_en_juego = 2
    for i in range(resultados.__len__()):
        if dinero_a_apostar > dinero_en_juego:
            if resultados[i] in numeros_elegidos:
                dinero_a_apostar += dinero_en_juego
                dinamica_dinero.append(dinero_a_apostar)
                dinero_en_juego += 1
            else:
                dinero_a_apostar -= dinero_en_juego
                dinamica_dinero.append(dinero_a_apostar)
                dinero_en_juego = 2
        else:
            dinamica_dinero.append(0.0)
    if dinamica_dinero[dinamica_dinero.__len__() - 1] == 0:
        print('Banca Rota :(')

    return dinamica_dinero


def main():
    tiradas = int(input("Ingrese la cantidad de tiradas: "))
    corridas = int(input("Ingrese la cantidad de corridas: "))
    dinero_a_apostar = 0
    numeros_elegidos = []
    estrategia = ''
    dinamica_dinero = []

#   Opcionales
    op = int(input("Ingrese 1 para apostar dinero infinito o 2 para elegir el monto: "))
    if op == 1:
        dinero_a_apostar = 100000000
    if op == 2:
        dinero_a_apostar = int(input("Ingrese la cantidad de dinero a apostar: "))

    op = int(input("Ingrese la estrategia a utilizar: 1-Martingala, 2-D'Alembert, 3-Fibonacci, 4-Paroli : "))
    if op == 1:
        estrategia = 'm'
        op = int(input("Ingrese apuesta de 1-color, 2-cuarto, 3-linea, 4-par o impar, 5-numero único: "))
    elif op == 2:
        estrategia = 'd'
        op = int(input("Ingrese apuesta de 1-color, 4-par o impar: "))
    elif op == 3:
        estrategia = 'f'
        op = int(input("Ingrese apuesta de 1-color, 2-cuarto, 3-linea, 4-par o impar, 5-numero único: "))
    elif op == 4:
        op = int(input("Ingrese apuesta de 1-color, 4-par o impar: "))
        estrategia = 'p'

    if op == 1 and (estrategia == 'd' or estrategia == 'm' or estrategia == 'f' or estrategia == 'p'):
        print("Rojo: [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]")
        print("Negro: [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]")
        op2 = int(input("Ingrese 1-Rojo, 2-Negro: "))
        if op2 == 1:
            numeros_elegidos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        else:
            numeros_elegidos = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    elif op == 2 and (estrategia == 'm' or estrategia == 'f'):
        print("Primer cuarto: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]")
        print("Segundo cuarto: [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]")
        print("Tercer cuarto: [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] ")
        op2 = int(input("Ingrese 1-1er Cuarto, 2-2do Cuarto, 3-3er Cuarto: "))
        if op2 == 1:
            numeros_elegidos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        elif op2 == 2:
            numeros_elegidos = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        elif op2 == 3:
            numeros_elegidos = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    elif op == 3 and (estrategia == 'm' or estrategia == 'f'):
        print("Primera linea: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]")
        print("Segunda linea: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]")
        print("Tercera linea: [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34] ")
        op2 = int(input("Ingrese 1-1er linea, 2-2da linea, 3-3ra linea: "))
        if op2 == 1:
            numeros_elegidos = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        elif op2 == 2:
            numeros_elegidos = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        elif op2 == 3:
            numeros_elegidos = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    elif op == 4 and (estrategia == 'd' or estrategia == 'm' or estrategia == 'f' or estrategia == 'p'):
        print("Par: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]")
        print("Impar: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]")
        op2 = int(input("Ingrese 1-Par, 2-Impar: "))
        if op2 == 1:
            numeros_elegidos = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        elif op2 == 2:
            numeros_elegidos = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
    elif op == 5 and (estrategia == 'm' or estrategia == 'f'):
        numero_elegido = int(input("Ingrese numero del 0 al 36"))
        numeros_elegidos.append(numero_elegido)


    resultados = []
    for _ in range(corridas):
        resultado = simulacion(tiradas)
        resultados.extend(resultado)

    tiradas_y_corridas = list(range(corridas*tiradas))

#   Estrategias

    if estrategia == 'm':
        dinamica_dinero = martingala(resultados, numeros_elegidos, dinero_a_apostar)
    elif estrategia == 'd':
        dinamica_dinero = dalambert(resultados, numeros_elegidos, dinero_a_apostar)
    elif estrategia == 'f':
        dinamica_dinero = fibonacci(resultados, numeros_elegidos, dinero_a_apostar)
    elif estrategia == 'p':
        dinamica_dinero = paroli(resultados, numeros_elegidos, dinero_a_apostar)


#   Graficas
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.set_xlabel("Dinero")
    ax.set_ylabel("Repeticiones")
    if estrategia == 'm':
        ax.set_title("Martingala")
    elif estrategia == 'd':
        ax.set_title("D'Alembert")
    elif estrategia == 'f':
        ax.set_title("Fibonacci")
    elif estrategia == 'p':
        ax.set_title("Paroli")

    ax.plot(tiradas_y_corridas, dinamica_dinero)
#    plt.savefig("Paroli-DI.png")
    plt.show()

    print(dinamica_dinero)


if __name__ == "__main__":
    main()

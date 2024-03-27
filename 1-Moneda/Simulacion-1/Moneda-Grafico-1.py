import random
import matplotlib.pyplot as plt

random_values = [random.random() for _ in range(100)]
constants_values = [0.5 if i % 2 == 0 else 0.7 for i in range(100)]
plt.figure(figsize=(10,6))
plt.plot(random_values, label="Valores Aleatorios", color='blue')
plt.plot(constants_values, label="Valores Constantes", linestyle= '--' , color = 'red')
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.title("Grafico de valores aleatorios con valores constantes intermitente")
plt.legend()
plt.grid('true')
plt.show()
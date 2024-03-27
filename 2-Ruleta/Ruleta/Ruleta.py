import random
import matplotlib.pyplot as plt
import numpy as np

resultados = []

for i in range(10):
    contador = 0
    for j in range(5):
        valor = random.randint(0,36)
        resultados.append(valor)
        if valor == 17:
            contador += 1

total_resultados = len(resultados)
frecuencia_relativa = [resultados.count(i) / total_resultados for i in range(37)]

valor_promedio = np.mean(resultados)

desvio_estandar = np.std(resultados)

varianza = np.var(resultados)


fig, axs = plt.subplots(4, 1, figsize=(10, 20))

axs[0].plot(range(37), frecuencia_relativa, color='blue')
axs[0].set_title('Frecuencia Relativa')
axs[0].set_xlabel('Valor')
axs[0].set_ylabel('Frecuencia Relativa')

axs[1].axhline(y=valor_promedio, color='green', linestyle='--')
axs[1].set_title('Valor Promedio')
axs[1].set_xlabel('Valor')
axs[1].set_ylabel('Valor Promedio')

axs[2].axhline(y=desvio_estandar, color='orange', linestyle='--')
axs[2].axhline(y=-desvio_estandar, color='orange', linestyle='--')
axs[2].set_title('Desvío Estándar')
axs[2].set_xlabel('Valor')
axs[2].set_ylabel('Desvío Estándar')

axs[3].axhline(y=varianza, color='purple', linestyle='--')
axs[3].set_title('Varianza')
axs[3].set_xlabel('Valor')
axs[3].set_ylabel('Varianza')


plt.tight_layout()
# plt.savefig('Gráficas-Ruleta.png')
plt.show()
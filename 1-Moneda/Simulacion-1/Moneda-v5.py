import random
import sys

if len(sys.argv) !=3 or sys.argv[1] != "-n":
    print("Uso: python Moneda-v5.py -n <num_valores>")
    sys.exit(1)
num_valores = int(sys.argv[2])
valores = [random.randint(0,1) for i in range(num_valores)]
frecuencia_absoluta = {0:valores.count(0), 1:valores.count(1)}
frecuencia_relativa = {0: frecuencia_absoluta[0]/num_valores, 1:frecuencia_absoluta[1]/num_valores}

print("Valores Generados: ", num_valores)
print("Frecuencia Absoluta de 0", frecuencia_absoluta[0])
print("Frecuencia Absoluta de 1", frecuencia_absoluta[1])
print("Frecuencia Relativa de 0", frecuencia_relativa[0])
print("Frecuencia Relativa de 1", frecuencia_relativa[1])
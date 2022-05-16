# @Author SHarmelyn Violeta Bautista Luque
# e-mail: sbautistal@ulasalle.edu.pe
# Implementando la función iterativa, recursiva y recursiva con memoria
import math
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime


def fibo_iterativo(posicion, en_pantalla):
    fibo0 = 0
    fibo1 = 1
    for x in range(posicion + 1):
        if en_pantalla:
            print("F(", x, ") = " + str(fibo0) + "\n", end="\n")
        auxiliar = fibo0
        fibo0 = fibo1
        fibo1 = fibo1 + auxiliar
    return auxiliar


def fibo_recursivo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_recursivo(n-1) + fibo_recursivo(n-2)


def fibo_recursivo_memoria(arr, n):
    if n == 0:
        arr[0] = 0
        return 0
    if n == 1:
        arr[1] = 1
        return 1
    else:
        if(arr[n] == -1):
            arr[n] = fibo_recursivo_memoria(
                arr, n-1) + fibo_recursivo_memoria(arr, n-2)
            print(arr)
            return arr[n]
        else:
            return arr[n]


posicion = int(input("Ingrese la posicion  a calcular: "))
print(type(posicion))

k = 1

# definimos el tiempo de ejecucion de la funcion

while (k < 20):
    inicio = datetime.now().microsecond
    arr = []
    for x in range(0, k+1):
        arr.append(-1)

    print("\nImprimiendo la  serie de fibonacci con memoria: ")

    fibnew = fibo_recursivo_memoria(arr, k)
    fin = datetime.now().microsecond

# guardamos el tiempo de ejecucion en un archivo de texto plano

    duracion = format(fin - inicio)
    print('Duracion: {}'.format(fin - inicio))
    archivo = open("data1.txt", "a")
    archivo.write(str(k) + " " + duracion + "\n")

    print("Imprimiendo la  serie de fibonacci de forma  iterativa: ")

    inicio = datetime.now().microsecond
    fibo_iterativo(k, True)
    fin = datetime.now().microsecond

    duracion = format(fin - inicio)
    archivo = open("data2.txt", "a")
    archivo.write(str(k)+" " + duracion + "\n")

    inicio = datetime.now().microsecond
    fibonacci = fibo_recursivo(k)
    fin = datetime.now().microsecond

    duracion = format(fin - inicio)
    archivo = open("data3.txt", "a")
    archivo.write(str(k)+" " + duracion + "\n")
    print("FIbonacci de manera recursiva: \n")
    print(fibonacci)

    k += 1

# esta parte es para la lectura
# definimos los arrays que usaremos luego para el plot
array1 = []
array2 = []
array3 = []
array4 = []
array5 = []
array6 = []

# abrimos el archivo
archivo = open('data1.txt')
linea = archivo.readline()  # leemos el archivo
while linea != '':
    numeros = linea.split()  # convertimos la linea en un array con sus elementos
    # insertamos el primer elemento a nuestro array1
    array1.append(int(numeros[0]))
    # insertamos el segundo elemento anuestro array2
    array2.append(int(numeros[1]))
    linea = archivo.readline()

archivo = open('data2.txt')
linea = archivo.readline()
while linea != '':
    numeros = linea.split()
    array3.append(int(numeros[0]))
    array4.append(int(numeros[1]))
    linea = archivo.readline()

archivo = open('data3.txt')
linea = archivo.readline()
while linea != '':
    numeros = linea.split()
    array5.append(int(numeros[0]))
    array6.append(int(numeros[1]))
    linea = archivo.readline()

plt.plot(array1, array2)
plt.plot(array3, array4)
plt.plot(array5, array6)

plt.legend(['Memoria','Iterativo','Recursivo'], loc="upper left")
plt.title("Fibonacci")

plt.show()

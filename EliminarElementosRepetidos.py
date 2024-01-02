"""Programa para eliminar los elementos repetidos de un vector y para hallar el mayor valor."""

from ValidacionDatos import *
from numpy import *

# Cargar la lista con números enteros.
# Recorrer la lista comparando todos los elementos.
# Eliminar los elementos repetidos.
# Imprimir ambas listas para comparar.

# Función para cargar una lista con datos numéricos.
def crearListaEnteros():

    lista = [ ]                                     # Lista que se retorna cargada.
    while True:
        print("\t1. Ingresar un nuevo dato.", "\n",
              "\t2. Salir.", "\n")

        # Variable donde se almacena a opción seleccionada por el usuario.
        opcion = ValidarEntero("Seleccione una opción: ", "Error, seleccione una opción correcta.")

        if opcion == 1:
            # Variable donde se almacenan los datos ingresados por el usuario para cargar la lista.
            nuevoDato = ValidarEntero("Ingrese un número entero: ", "Error, ingrese un número entero.")

            lista.append(nuevoDato)

        elif opcion == 2:
            break

        else:
            continue

    return lista


def hallarMayor(lista):

    valorMayor = lista[0]              # Asumimos que el primer elemento de la lista es el mayor valor.

    for i in lista:                    # Recorremos la lista comparando todos sus elementos, buscando el mayor valor.
        if i > valorMayor:
            valorMayor = i

    valorMenor = min(lista)

    print("El mayor valor de la lista es: ",valorMayor)
    print("El menor valor de la lista es: ", valorMenor)

    vector1 = array(lista)
    print("La posición del mayor valor es: ",argmax(vector1))   # Hallamos el indice del mayor valor.

def compararElementos(lista):

    listaUnicos = [ ]                  # Lista con elementos sin repetir.
    for i in lista:
        if i not in listaUnicos:
            listaUnicos.append(i)

    print("Lista sin elementos repetidos: ",listaUnicos)

lista = [ ]                            # Lista para almacenar los datos ingresados por el usuario.
lista = crearListaEnteros()
print("Lista original: ",lista)
hallarMayor(lista)                     # Llamamos la función para hallar el mayor valor.
compararElementos(lista)





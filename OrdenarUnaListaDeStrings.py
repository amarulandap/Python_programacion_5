from random import *
from ValidacionDatos import ValidarEntero

"""Función para ordenar una lista de strings, con base en la longitud de las cadenas de caracteres."""

# Crear la lista de strings.
# Obtener la longitud de cada string.
# Crear una segunda lista con la longitud de las cadenas.
# Combinar ambas listas y ordenarla de manera ascendente.

def ordenarListacadenas(listaCadenas):

    # Creamos un ciclo para recorrer la lista de cadenas.
    listaLongitudes = [ ]
    for i in range(0, len(listaCadenas), 1):
        longitudes = len(listaCadenas[i])       # Almacenamos la longitud de cada una de las cadenas de la lista.
        listaLongitudes.append(longitudes)      # Agregamos a la lista de longitudes cada uno de los valores.

    # Combinamos ambas listas.
    listaCombinada = list(zip(listaLongitudes, listaCadenas))
    listaCombinada.sort()                       # Ordenamos la lista con comparando el primer elemento de cada pareja.

    print("Cadenas: ",listaCadenas, '\n',
          "Longitudes: ",listaLongitudes, '\n',
          "Combinación: ",listaCombinada)


"""Función para crear un vector con números aleatorios en un rango específico."""

# Determinar la longitud del vector.
# Determinar el límite inferior y el límite superior.
# Ordenar el vector de manera descendente.
# Obtener una muestra de dicho vector.

def obtenerMuestra (vector):

    vectorMuestra = [ ]                            # Almacenar la muestra tomada del vector original.
    for i in vector:
        if i not in vectorMuestra:                 # Validamos que el dato no se encuentre en el vector muestra.
            vectorMuestra.append(i)

    vectorMuestra1 = sample(vector, 10)        # Obtenemos una muestra real con el número de datos que definamos.

    print("Muestra: ",vectorMuestra)
    print("Muestra 1: ",vectorMuestra1)

def vectorAleatorio(longitud, limiteInferior, limiteSuperior):

    vector = [ ]
    for j in range(0, longitud, 1):
        nuevoValor = randint(limiteInferior, limiteSuperior)
        vector.append(nuevoValor)

    vector.sort()
    vector.reverse()                                # Ordenamos el vector de manera descendente.
    print("Vector de números aleatorios: ",vector)

    obtenerMuestra(vector)


listaCadenas = ['Cali', 'Medellin', 'Bogotá', 'Barranquilla', 'Santa Marta', 'Pereira', 'Manizales', 'Mitú','Leticia', 'Rioacha']
ordenarListacadenas(listaCadenas)

print('\n')
longitud = ValidarEntero("Ingrese la longitud del vector: ", "Error, ingrese un número entero.")
limiteInferior = ValidarEntero("Ingrese el límite inferior: ", "Error, ingrese un valor correcto.")
limiteSuperior = ValidarEntero("Ingrese el límite superior: ", "Error, ingrese un valor correcto.")
vectorAleatorio(longitud, limiteInferior, limiteSuperior)

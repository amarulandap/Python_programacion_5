from ValidacionDatos import *

"""1. Programa para sumar los componentes pares de un vector"""

# Cargar el vector con datos numéricos.
# Validar que los datos si sean numéricos.
# Validar que el dato sea un número par.
# Sumar los números pares.
# Mostrar el resultado en pantalla.


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

# Función para validar números pares.
def numerosPares(numero):

    if numero % 2 == 0:
        numeroPar = True
    else:
        numeroPar = False                         # Variable que indica que el número es par.

    return numeroPar

# Función para sumar los números pares.
def sumarPares(lista):

    sumaPares = 0                               # Variable para almacenar la suma.

    for i in lista:                             # La variable i almacena cada uno de los valores de la lista.
        numeroPar = numerosPares(i)             # Almacenamos lo que retorna la validación.

        if numeroPar:
            sumaPares += i

    print("suma números pares = ",sumaPares)


# Programa principal.
lista = [ ]
lista = crearListaEnteros()
sumarPares(lista)
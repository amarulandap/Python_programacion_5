"""Programa para generar la secuencia de Ulam."""

from ValidacionDatos import ValidarEntero

# Solicitar el ingreso de un número natural.
# Si el número x es impar -- 3x + 1.
# Si el número x es par -- x / 2.
# La secuencia de números terminará cuando el número generado sea 1.
# El dato inicial no se incluye en la sucesión.

def validarPar(numero):                 # Función para validar que el número generado en la secuencia es o no par.

    if numero % 2 == 0:
        numeroPar = True
    else:
        numeroPar = False

    return numeroPar

while True:

    # Pedimos al usuario que ingrese el dato inicial.
    datoInicial = ValidarEntero("Ingrese un número natural: ", "Error, debe ingresar un número natural.")

    # Validamos que si sea un número natural.
    if datoInicial < 1:
        print("Error, debe ingresar un número natural.")
        continue

    sucesionUlam = [ ]                          # Almacenar los datos generados en la sucesión.
    if datoInicial == 1:
        print("Dato inicial = ",datoInicial," : ",sucesionUlam)
    else:
        resultado = datoInicial                 # Almacenar el resultado de cada ecuación.
        while resultado != 1:
            validacion = validarPar(resultado)  # Variable booleana que indica si el número es par o impar.
            if validacion:
                resultado /= 2
            else:
                resultado = 3 * resultado + 1

            sucesionUlam.append(resultado)

        sucesionUlam.reverse()                  # Invertir el orden de los números generados.
        print("Dato inicial = ",datoInicial, " : ",sucesionUlam)
    break

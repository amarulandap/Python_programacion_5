from ValidacionDatos import *
from random import *

"""Programa para simular los saltos de un conjunto de ranas."""

#1. Determinar la longitud de la pista.
#2. Determinar el número de ranas.
#3. Inicializar en 0 el vector de saltos de las ranas y el contador de saltos.
#4. Simular el salto de la rana 0 y sumarlo a la posición 0 del vector.
#5. aumentar en 1 el contador de saltos.
#6. Comparar el valor acumulado por la rana 0 con la longitud de la pista y si es mayor terminar el programa.
#7. Mostrar en pantalla la rana ganadora y el número de saltos.

# Determinar la longitud de la pista.
longitudPista = ValidarReal("Ingrese la longitud de la pista en metros: ", "Error, ingrese un número.")

# Determinar el número de ranas.
while True:
    ranas = ValidarEntero("Ingrese el número de ranas: ", "Error, ingrese una cantidad correcta.")

    if ranas < 0:
        print("Error, ingrese una cantidad correcta.")
        continue

    break

# Inicializar el vector de ranas y el contador de saltos.
vectorRanas = [ ]
saltosRanas = [ ]

for i in range(ranas):
    vectorRanas.append(0)
    saltosRanas.append(0)

# Simular los saltos de las ranas.
saltoRana = 0                                # Almacenar cada uno de los saltos de las ranas.
while True:

    for i in range(0, len(vectorRanas)):    # Simula cada uno de los saltos de las ranas.
        saltoRana = randint(0,2)
        vectorRanas[i] += saltoRana
        saltosRanas[i] += 1

    if vectorRanas[i] >= longitudPista:
        break

print("La rana en la posición",i+1, "saltó: ",vectorRanas[i], "metros en ",saltosRanas[i])


"""Programa para controlar la venta de entradas a un concierto"""

#1. Ingresar la cantidad de boletos disponibles para el concierto.
#2. Crear el vector de identificaciones.
#3. Leer la identificación de cada uno de los compradores y agregarla al vector.
#4. Si el número de identificación ya está en el vector, rechazar la venta.
#5. Si la venta es posible, restringir el número de boletos a máximo 4 y restar los comprados de los boletos disponibles.
#5.1. Generar un mensaje indicando la cantidad de boletos disponibles.
#6. Finalizar el programa cuando la venta llegue a cero.

print("\n")
# Cantidad de boletos inicial.
aforo = ValidarEntero("Ingrese la cantidad de boletos a vender: ", "Error, ingrese una cantidad correcta.")

# Vector de identificaciones.
identificaciones = [ ]

while aforo > 0:

    identificacion = ValidarEntero("Ingrese el número de cédula(sin puntos ni comas): ", "Error, ingrese el número correcto.")

    if identificacion not in identificaciones:              # Si la identificación no se encuentra en el vector, la agrega.
        identificaciones.append(identificacion)

        while True:                                         # Controlar que la cantidad de boletos comprados sea correcta.
            cantidadBoletos = ValidarEntero("Cantidad de boletos(máximo 4): ", "Error, ingrese uns cantidad correcta.")

            if cantidadBoletos < 0 or cantidadBoletos > 4 or cantidadBoletos > aforo:
                print("Error, ingrese una cantidad correcta.")
                continue

            break

        aforo -= cantidadBoletos
        print("Boletos disponibles: ",aforo)

    else:                                                  # Si la identificación ya está en el vector, rechaza la venta.
        print("Venta rechazada, cliente ya adquirió boletas.")
        continue

print("Boletos agotados.", aforo," disponibles.")




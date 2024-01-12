from ValidacionDatos import *
from random import *

"""Programa para determinar cuántas cajas tienen un peso mayor al peso promedio."""

# 1. Crear la lista de los pesos.
# 2. Hallar el peso promedio.
# 3. Recorrer la lista y comparar el peso de cada caja con el promedio.
# 4. Si el peso es mayor al promedio, agregarlo a una nueva lista.
# 5. Determinar el tamaño de la nueva lista.
# 6. Mostrar ambos en pantalla.

listaPesos = [120.5, 85.4, 75, 20.8, 55, 60.7, 70, 36.9, 66, 100.25]

promedioPesos = sum(listaPesos) / len(listaPesos)       # Dividimos la sumatoria de los pesos entre el tamaño de la lista.

pesosMayores = [ ]                                      # Lista para almacenar los pesos mayores al promedio.
for i in listaPesos:                                    # Recorremos la lista buscando los pesos mayores al promedio.
    if i > promedioPesos:
        pesosMayores.append(i)

print("Lista de pesos: ", listaPesos, "\n",
      "Peso promedio: ",format(promedioPesos, ".3f"),"\n",
      "Pesos mayores que el promedio: ",pesosMayores,"\n",
      "Número de cajas con peso mayor al promedio: ",len(pesosMayores))


"""Programa para generar una muestra de paquetes en una bodega."""

# 1. Ingresar el número de paquetes.
# 2. Generar una lista ordenada de manera ascendente entre 1 y n.
# 3. Calcular el 10% del número de paquetes.
# 4. Generar una muestra cuyo tamaño sea igual al 10%.
# 5. Imprimir ambas listas.

print('\n')
while True:
    numeroPaquetes = ValidarEntero("Ingrese el número de paquetes: ", "Error, ingrese un número mayor que 0.")

    if numeroPaquetes < 1:
        print("Error, ingrese un número mayor que 0.")          # Garantizando que en la bodega hay 1 o mas paquetes.
        continue

    listaPaquetes = [ ]                                         # Lista de paquetes numerados.
    for i in range(1, numeroPaquetes + 1, 1):
        listaPaquetes.append(i)

    tamañoMuestra = len(listaPaquetes) // 10                    # Calculamos el 10% que es el tamaño de la muestra.
    listaMuestra = sample(listaPaquetes, tamañoMuestra)         # Lista de datos de la muestra.

    print("Lista paquetes: ", listaPaquetes,"\n",
          "Muestra: ", listaMuestra)

    break


"""Programa para asignar aleatoriamente los contenedores de una bodega."""

# 1. Conocer el número de contenedores.
# 2. Calcular el número de inspectores.
# 3. Crear una lista con el total de contenedores (suponer que los contenedores estan numerados consecutivamente).
# 4. Tomar una muestra de dos elementos de la lista de contenedores.
# 5. Asignar esos dos contenedores a un inspector.
# 6. Mostrar en pantalla la dupla inspector - contenedores.
# 7. Eliminar los contenedores de la lista.
# 8. Repetir el proceso hasta que la lista de contenedores este vacia.

print('\n')
# Pedir al usuario que ingrese el número de contenedores.
numeroContenedores = ValidarEntero("Ingrese el número de contenedores: ", "Error, ingrese un número entero mayor que 0.")

# calculamos el número de inspectores.
inspectores = numeroContenedores // 2

# Lista de contenedores.
listaContenedores = [ ]
for i in range(1, numeroContenedores + 1):
    listaContenedores.append(i)

# generar muestras de 2 contenedores y las asignamos a cada inspector.
while len(listaContenedores) > 1:
    for i in range(1, inspectores + 1):
        muestraInspeccion = sample(listaContenedores,2)
        # Imprimir la pareja inspector - contenedores.
        print("Inspector ",i ,"Contenedores: ",muestraInspeccion[0], "-", muestraInspeccion[1])
        listaContenedores.remove(muestraInspeccion[0])
        listaContenedores.remove(muestraInspeccion[1])          # Eliminamos los contenedores que ya fueron asignados.


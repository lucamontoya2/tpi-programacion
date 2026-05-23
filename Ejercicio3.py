# Parte B — Implementación en Python
# 3. Calcular:

# o El tiempo promedio de ejecución por función
# o El tiempo promedio de ejecución por servidor 

funcion = 3
servidor = 3



matriz = []


# CARGA DE VECTORES

for i in range(funcion):
    vector = [0] * servidor
    matriz.append(vector)
    for j in range(servidor):
        valor = int(input("Ingrese los valores del vector:  "))
        vector[j] = valor

# MOSTRAR MATRIZ

for fila in matriz:
    print(fila)

# PROMEDIO

for j in range(servidor):

    suma = 0

    for i in range(funcion):
        suma = suma + matriz[i][j]

    promedio = suma // funcion

    print("\nEl promedio del servidor", j, "=", promedio, end=" ")
    print()
print("\n")

for i in range(funcion):

    vector = matriz[i]

    suma = 0

    for valor in vector:
        suma = suma + valor

    promedio = suma // servidor

    print("\nEl promedio de la funcion", i,"=", promedio)
print("\n")

transpuesta = []

for i in range(servidor):
    fila = []
    
    for j in range(servidor):
        valor = matriz[j][i]
        fila.append(valor)
                    
    
    transpuesta.append(fila)

for valor in transpuesta:
    print(valor)
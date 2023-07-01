nombre = "carlos"
edad= 29
estatura = 1.70
baila = False
print(nombre)
print(edad)
print(estatura)
print(baila)

nombre_edad= nombre + str(edad)
nombre_estatura= nombre + str (estatura)
nombre_baila =nombre + str (baila)
print(nombre_edad)
print(nombre_estatura)
print(nombre_baila)

#El tipo de los números enteros es int. Este tipo de dato comprende el conjunto de todos los números enteros, pero como dicho conjunto es infinito, en Python el conjunto está limitado realmente por la capacidad de la memoria disponible. No hay un límite de representación impuesto por el lenguaje.
#Puedes usar el tipo float sin problemas para representar cualquier número real (siempre teniendo en cuenta que es una aproximación lo más precisa posible). Por tanto para longitudes, pesos, frecuencias,en los que prácticamente es lo mismo 3,3 que 3,3000000000000003 el tipo float es el más apropiado.

# Aplica la fórmula de la suma de los primeros n números pares (investigar), 
# tomando como n la variable de tipo entero y almacenar el resultado en una variable

suma = 0
n = 1
while n != 0:
    n = int(input("ingresa un numero"))
    if n != 0:
        if n % 2 == 0:
            suma = suma + n
print("la suma de los numeros es: ",suma)
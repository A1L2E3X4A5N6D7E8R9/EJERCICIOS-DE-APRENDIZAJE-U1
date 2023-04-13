###CURSO DE FUNDAMENTOS DE PYTHON
#1. Crear una lista de numeros del 1 al 5
numeros=[1,2,3,4,5]
print("los numeros de la lista son:", numeros)
#2. Accede al elemento 3 de la lista:
print("el elemento en la posicion 3 es:",numeros[27])
#3. Modifica un elemento de la lista:
numeros[3]=33
print("elemento modificado es:",numeros)
#4. Agrega el elemento 9 al final de la lista
numeros.append(9)
#5. Eliminar el elemento 2 de la lista:
numeros.pop(2)
#6. Recorrer una lista con un bucle for:
for e in numeros:
    print(e)
#7. Ordenar una lista:
numeros.sort(reverse=False)
print(numeros)
#8. Obtener la longitud de una lista:
len(numeros)
#9. Comprobar si un elemento está en la lista:
num = input("ingrese un numero: ")
if num in numeros:
    print(f"El numero {num} esta en la lista")
else:
    print(f"El numero {num} no esta en la lista") 
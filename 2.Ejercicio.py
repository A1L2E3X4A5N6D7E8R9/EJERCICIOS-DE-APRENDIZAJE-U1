#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE LISTAS A RESOLVER
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
numeros= list()
for e in range(5):
    numeros.append(int(input("Introduce los numeros del 1 al 5: ")))    
print("Los numeros de la lista son:")
#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
nombres= list("mateo","javier","gabriela","alison","franklin")
nombres(0)
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
digitos= list(1,2,3,4,5,6,7,8,9,10)
for e in digitos:
    if e%2 ==0:
        print("los numeros pares son:",e)
#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
nombres= list("mateo","javier","gabriela","alison","franklin")
nombres[-1]
#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
digitos= list(1,2,3,4,5,6,7,8,9,10)
digitos[-1]
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
digitos= list(1,2,3,4,5,6,7,8,9,10)
for e in digitos:
    if e%2 ==1:
        print("los numeros impares son:", e)
#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
nombres= list("mateo","javier","gabriela","alison","franklin")
nombres.append("EMY")
nombres
#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
digitos= list(1,2,3,4,5,6,7,8,9,10)
digitos[0,-1]
#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
nombres= list("mateo","javier","gabriela","alison","franklin")
len(nombres)
#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
digitos= list(1,2,3,4,5,6,7,8,9,10)
operacion=0
for e in digitos:
    if e<=10:
        operacion=e+operacion
    print("la suma de los elemtos son:", operacion)


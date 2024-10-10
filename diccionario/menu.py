import os
os.system("cls")

def  menu():
    print("\n----Menú----")
    print("1. suma los numeros de una lista")
    print("2. Contar las vocales, consonantes y caracteres especiales de una frase")
    print("3. crear una matriz nxn y llenar sus diagoanles")
    print("imprima X para salir")

#opcion 1

def suma_lista():
    numeros = []
    while True:
        entrada = input("ingrese un número (o presiones enter para terminar):")
        if entrada == '':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Error: no es un número, ingrese un número válido.")

    suma = sum(numeros)
    print(f"La suma de los números es: {suma}")


#opcion 2
def contar_caracteres():
    frase = input("ingrese una frase:")
    vocales = "aeiouAEIOU"
    contVocales = sum(1 for char in frase  if char in vocales)
    contConsonantes = sum(1 for char in frase if char.isalpha() and char not in vocales)
    #contOtros = sum(1 for char in frase if not char.isalpha())
    contOtros = len(frase) -  (contVocales + contConsonantes)


    """ vocales_count = 0
    consonantes_count = 0
    especiales_count = 0
    for character in frase:
        if(character in vocales):
            vocales_count += 1
        elif character.isalpha():
            consonantes_count += 1
        else:
            especiales_count += 1
 """
    
   
    print(f"vocales: {contVocales}, cosonantes: {contConsonantes},  especiales: {contOtros}")



#opcion 3
def crear_matriz():
    n = int(input("ingrese el tamaño de la matriz:"))
    matriz = ["" * n for _  in range(n)]

    for i in range(n):
        row = []
        for j in range(n):
            if  i == j or  i+j == n-1:
                row.append("*")
            else:
                row.append(" ")
        matriz.append(row)


    print(matriz)
      





#Programa principal

while  True:
    menu()



    opcion = input("ingrese una opción: ").strip().upper()

    if opcion == '1':
        suma_lista()
    elif  opcion == '2':
        contar_caracteres()
    elif  opcion == '3':
        crear_matriz()

    elif opcion == 'X' or 'x':
        print("adiós")
        break





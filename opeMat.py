"""
un programa con las operaciones basicas y complejas de aritmetica
"""
#definir variables

num1 = float(input("ingrese un numero:"))
num2 = float(input("ingrese un numero:"))

#sumar
suma = num1 + num2
print(f"el resultado de la suma es: {suma}")

resta = num1 - num2
print(f"el resultado de la resta es: {resta}")

multiplicacion = num1 * num2
print(f"el resultado de la multliplicacion es: {multiplicacion}")

if num2 != 0: 
    division = num1/num2
    print(f"el resultado de la division es: {division}")

else: 
    print("no se puede dividir por cero")

potencia = num1**num2
print(f"el resultado de la potencia es: {potencia}")

if num1 >= 0 and num2 > 0:
    raiz = num1 ** (1/num2)
    print(f"el resultado de la raiz es: {raiz}")

else:
    print("esta operacion no es valida")


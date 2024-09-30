numero = int(input("Ingresa un nÃºmero para calcular su factorial: "))
factorial = 1
contador = 1
while contador <= numero:
    factorial *= contador
    contador += 1
print("El factorial de", numero, "es:", factorial)
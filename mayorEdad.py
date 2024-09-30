nombre = str(input("nombre: "))
edad = int(input("edad: "))
documento = input("documento: ").lower()

if ((edad >= 18) and (documento == "si")):
    print("puede entrar")
else:
    print("no puede entrar")



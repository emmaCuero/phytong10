
while True:


  palabra = input("ingrese una palabra: ")
  letraInicial = input("ingrese la letra inicial: ")

  if palabra[0:2].lower() == letraInicial.lower():
    print(f"la palabra {palabra} comienza con la letra {letraInicial} ingresada")
  else:
    print(f"la palabra {palabra} no comienza con la letra {letraInicial} ingresada")




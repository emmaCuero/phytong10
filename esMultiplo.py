def es_multiplo():
    try:
        num1 = int(input("ingrese el primer numero: "))
        num2 = int(input("ingrese el segundo numero: 90"))

        if num2 == 0:
            raise ValueError("error, no se puede dividir por cero")

        if num1 % num2 == 0:
            print(f"el numero {num1} es múltiplo del numero {num2}")

        else:
            print(f"el numero {num1} no es múltiplo del numero {num2}")


    except ValueError as ve:
        print("error!",ve)
    except Exception as ex:
        print("error!, inesperado", ex)

es_multiplo()


import math
def calcularAreaPerimetro():
    try:
        radio = float(input("ingrese el radio: "))

        if radio < 0:
            raise ValueError("el radio no puede ser negativo!")
        
        #area = math.pi * (pow(radio))
        area2 = math.pi * (radio ** 2)

        perimetro = 2 * math.pi * radio

        #print(f"area del circulo es: {area:.2f}")
        print(f"area2 del circulo es: {area2:.2f}")
        print(f"perimetro del circulo es: {perimetro:.3f}")

    except ValueError as e:
        print(f"error : {e}")
    except Exception as e:
         print(f"error, inesperado : {e}")


calcularAreaPerimetro()
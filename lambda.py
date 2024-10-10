# Funciones Lambda

""" x = lambda a: a * 2

print(x(6))

m = lambda a, b: a + b
print(m(6,8))

l = lambda a, b, c: a  + b + c
print(l(3,5,8)) """

def miFuncion(n):
    return lambda a: a * n 

miSalida = miFuncion(2)
print(miSalida(5))


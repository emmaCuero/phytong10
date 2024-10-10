#diferencias entre conjuntos y listas

""" conjunto = {1,4,7,68,76,76,1,3,2,4}
print(conjunto)
print(len(conjunto))
print(type(conjunto))

otroConjunto = set(("este", "es", "un", "conjunto"))
print(otroConjunto) """

""" if conjunto not in otroConjunto:
    print("el conjunto no está en otro conjunto")
else:
     print("el conjunto está en otro conjunto") """

""" otroConjunto.add("cadenas")


otroConjunto.update()
print(otroConjunto)
 """

a = {1,2,3,4,5}
b = {1,3,5,7,9}

""" u = a.union(b)
print(u)

u2 = a|b #union
print(u2)
#a.update(b) -> modifica el conjunto original """

""" i = a.intersection(b)
print(i)

i2 = a & b
print(i2) """

d = a.difference(b)
print(d)

d2 = a - b
print(d2)


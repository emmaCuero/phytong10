miDiccionario = {
    "nombre" : "Emmanuel",
    "email":"manuelfc1990@gmail.com",
    "edad" : 23,
    "miniDic" : {
        "estadoC":"casado",
        "sexo":"masculino"
    },
    "lista":["rojo", "azul", "verde"]
}


""" print(miDiccionario)
print(miDiccionario["miniDic"]) """

#agregar valor, clave-valor
miDiccionario["cargo"]="Estudiante"

print(miDiccionario)

#eliminar valor
del miDiccionario["edad"]
print(miDiccionario)

if "nombre" in miDiccionario:
    print(f"la clave 'nombre' existe")

#Cree su propio diccionario
#.get(), obtiene el valor si existe clave
#.pop(), elimina y devuleve el valor
#.update({clave: valor,  clave2: valor2}), agrega o actualiza valores
#Ej. crear una funcion que reciba un diccionario y retorne la lista de los valores
#Ej2. Una funcion que reciba un diccionario y retorne una lista de tuplas, 
# donde cada tupla contiene la clave y el valor
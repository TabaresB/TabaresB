#creando una lista (se puede modificar )
lista=["kevin steven","Tabares Blanco",22,"BOGOTA"]
print(lista[3])
#creando una tupla (no se puede modificar )
tupla=("kevin steven","Tabares Blanco",22,"BOGOTA")
print(tupla[2])

#esto es modificacion
lista[2]=500
print(lista[2])

#creando un se(conjunto)
#no tienen un orden fijo y pueden cambiar , tampoco hay datos duplicados 
conjunto={"kevin steven","Tabares Blanco",22,"BOGOTA"}


#creando un dict(diccionario)
#es igual que la lista pero en ves de darmelo en por el numero de indice me lo da es por el nombre
diccionario={
    "nombre" : "kevin",
    "apellido" : "Tabares",
    "edad" : 22,
    "ciudad" : "BOGOTA"

}

print(diccionario["edad"])
"""a=19
k=20
c=a + k
print(c)

nombre="gabriel"

print(nombre)


numero=20

numero//=2

print(numero)

nombre="gabriel "

saludo=nombre +" ¿hola como estas?"

print(saludo)

saludo="bien y tu ??" + nombre 

print(saludo)
"""
#concatenar con +
nombre=input("como te llamas?")

saludo="hola " + nombre + " ¿como estas?"

print(saludo)

#concatenar con f string
pronombre=input("como te llamas?")

bienvenida=f"hola {pronombre}¿como estas?"

print(bienvenida)

#Operadores de pertenencia in y not in
print("hola" in saludo)# True

print("como" not in bienvenida)# False 


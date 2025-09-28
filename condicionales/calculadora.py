'''
#Calculadora básica (suma, resta, multiplicación, división).
print(" bienvenido a la calculadora ")

a=(str(input("ingrese una sola accion suma, resta, multiplicacion o division ")))

if a=="suma":
    b=int(input("ingrese un numero para sumar "))
    c=int(input("ingrese otro numero para sumar "))
    print("el resultado de la suma es ", b+c)

elif a=="resta":
     b=int(input("ingrese un numero para resta "))
     c=int(input("ingrese otro numero para resta "))
     print("el resultado de la resta es ", b-c)

elif a=="multiplicacion":
     b=int(input("ingrese un numero para multiplicacion "))
     c=int(input("ingrese otro numero para multiplicacion "))
     print("el resultado de la multiplicacion es ", b*c)

elif a=="division":
     b=int(input("ingrese un numero para division "))
     c=int(input("ingrese otro numero para division "))
     if c!=0:
          print("el resultado de la division es ", b/c)
     else:
          print("error no se puede dividir entre 0")

#area de un circulo
d=int(input("de el numero del radio para calcular el area del circulo"))
area=3.14*d**2

print("el area del circulo es ",area)

#nota de aprobado o reprobado 

nota=int(input("indique la nota"))

if nota>=50:
     print(" aprobado")
else:
     
     print("desaprobado")


#el modulo o resto funciona asi escogemos 2 valores que uno quiera dividir entre ellos y dependiendo del valor que este al lado del operador varia su resto 
a=12%5
print(a)
#Programa que pida un número y diga si es par o impar.

numero=int(input("ingrese un numero"))

if numero%2==0:
    print("su numero es par ")
else:
    print("su numero es impar")

a1=int(input("ingrese un numero "))
a2=int(input("ingrese otro  numero "))

if a1>a2:
    print(a1, "es mayor",a2)
else :
    print(a2,"es mayor que ",a1)
    '''

edad=int(input("ingrese su edad "))

if 0<= edad <=12 :
    print("es un niño")
elif 13<= edad <=17 :
    print("es un adolescente")
elif 18<= edad <=59 :
    print("es un adulto")
elif edad >=60 :
    print("es un adulto mayor ")

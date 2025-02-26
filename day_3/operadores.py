#Día 3 de python
#Puntos del 1 al 3
age=18
height=1.75
complex= (1+7j)

#Punto 4
base1=input("Escribe el valor de la base del triángulo: ")
base=int(base1)
altura=input("Escriba el valor de la altura del triángulo: ")
height=int(altura)
area=0.5* (base * height)
print("El área del triángulo es: ", area)

#Punto 5
a=input("Ingrese el valor del lado a del triángulo: ")
a1=int(a)
b=input("Ingrese el valor del lado b del triángulo: ")
b1=int(b)
c=input("Ingrese el lado c del triángulo: ")
c1=int(c)
perimetro= a1 + b1 +c1
print("El perímetro del triángulo es: ", perimetro)

#Punto 6
l=input("Ingrese el valor del largo del rectángulo: ")
lenght= int(l)
w=input("Ingrese el ancho del rectángulo: ")
width=int(w)
area1= lenght * width
print("El área del rectángulo es: ", area1)
perimetro1= 2* (lenght + width)
print("El perímetro del rectángulo es de: ", perimetro1)

#Punto 7
r=input("Ingresa el valor del radio del círculo: ")
radio=int(r)
area2= 3.14* (radio **2)
print("El área del círculo es: ", area2)
circumference= radio * 2 * 3.14
print("La circunferencia del círculo es: ", circumference)

#Punto 8
xint=int(input("Escribe la intercepción en X: "))
yint=(xint*2)-2
print("La intercepción en Y es:", yint)
print("Y la pendiente es: ",2)

#Punto 9
x1, x2, y1, y2 = 2, 6, 2, 10
print("Distancia: ")
print(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
print("Pendiente: ")
print((y2 - y1) / (x2 - x1))

#Punto 10
print(2 if 2 < (y2 - y1) / (x2 - x1) else (y2 - y1) / (x2 - x1))
#Punto 11
for x in range(-5, 5):
    print((x ** 2) + (6 * x) + 9)
print( -3, "is where y is 0")

#Punto 12
print(not len("python") == len("dragon"))

#Punto 13
print("on" in "pyhton" and "on" in "dragon")

#Punto 14
print("jargon" in "I hope this course is not full of jargon")

#Punto 15
not print( "no" in "dragon" and "on" in "python")

#Punto 16
print(str(float(len("python"))))

#Punto 17
number=int(input("Ingresa un número: "))
print("El número es Par" if (number % 2) == 0 else "No es par")

#Punto 18
value=int(2.7)
print(7//3 == value)

#Punto 19
print(type("10") == type(10))

#Punto 20
print(int(9.8) == 10) #Si ponemos el 9.8 como string marca error, puesto que no es unn valor con base 10

#Punto 21
hours=int(input("Ingresa las horas: "))
rate_per_hour=int(input("Ingresa la tarifa por hora: "))
print("El pago es de: $", hours * rate_per_hour)

#Punto 22
years=int(input("Ingresa la edad en años de la persona: "))
print("El tiempo en segundos que la persona puede vivir es de: ", years * 365 * 24 * 60 * 60 * 60)

#Punto 23
for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)
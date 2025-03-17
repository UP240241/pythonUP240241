#Punto 1
grade=int(input("Ingrese los puntos del estudiante: "))
if grade >= 90 and 100:
    print("La calificación es A")
elif grade >= 70 and 89:
    print("La calificación es B")
elif grade >= 60 and 69:
    print("La calificación es C")
elif grade >= 50 and 59:
    print("La calificación es D")
else:
    print("La calificación es F")

#Punto 2
month = input('Ingresa el mes: ').title()
if month in ["Septiembre", "Octubre", "Noviembre"]:
    print("La temporada es Otoño")
if month in ["Diciembre", "Enero", "Febrero"]:
    print("La temporada es Invierno")
if month in ["Marzo", "Abril", "Mayo"]:
    print("La temporada es Primavera")
if month in ["Junio","Julio","Agosto"]:
    print("La temporada es Verano")
    
#Punto 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit= input("Ingrese la fruta: ")
if fruit in fruits:
    print("Esta fruta ya existe en la lista")
else:
    fruits.append(fruit)
    print(fruits)
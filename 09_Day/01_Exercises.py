#Punto 1
age=int(input("Ingresa tu edad: "))
if age >= 18:
    print("Tienes la edad suficiente para aprender a manejar")
else:
    false= (18) - age
    print("Te faltan", false, "años para aprender a manejar")

#Punto 2
my_age= 18
if age == my_age:
    print("Tenemos la misma edad")
elif age < my_age:
    if age +1 == my_age:
        print("Eres menor que yo por un año")
    else:
        print("Eres menor que yo")
else: 
    if  age -1 == my_age:
        print("Eres mayor que yo por un año")
    else: 
        print("Eres mayor que yo")

#Punto 3
a=int(input("Ingresa el primer número: "))
b=int(input("Ingrese el segundo número: "))
if a > b:
    print(a,"Es más grande que ", b)
elif a == b:
    print(a, "Es igual a ",b)
else:
    print(a,"Es menor que ",b)

#Día 2 de programación en Python
#Ejercicios nivel 1, abarca del punto 1 al 13
apellido="Reséndiz"
nombre_completo="Ismael Reséndiz Esquivel"
pais="México"
ciudad="Aguascalientes"
edad=18
año=2006
is_married=False
is_true=True
is_light_on=True
carrera, grupo, cuatrimestre="Ingenieniería Mecatrónica", "B", 1

#Ejercicios nivel 2,abarca del punto 1 al 3
print(type(apellido))
print(type(nombre_completo))    
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(carrera))
print(type(grupo))
print(type(cuatrimestre))

print("Longitud de nombre: ", len(nombre_completo)), print("Longitud de apellido: ", len(apellido))
print("Nombre:", nombre_completo,  "es mayor que", apellido) 

#Abarca del punto 4 al 12
num_uno=5
num_dos=4
total=num_uno+num_dos
diff=num_uno-num_dos
producto=num_uno*num_dos
division=num_uno/num_dos
remainder=num_uno%num_dos
exp=num_uno**num_dos
floor_division=num_uno//num_dos
area_del_circulo=3.14*(30**2)
circunferencia_del_circulo=2*3.14*30
a=input("Escribe el radio: ")
radio = int(a)
area= 3.14*(radio ** 2)
print("El área del círculo es: ", area)

#Punto 13
first_name=input("Escribe el primer nombre:")
last_name=input("Escribe el apellido: ")
country=input("Ingresa el país: ")
age=input("Ingresa la edad: ")

#Punto 14
help('keywords')

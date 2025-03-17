#Variables
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Punto 1
print(len(set(age)))
print(len(age))
print(len(age) > len(set(age)))

#Punto 2
"""
La diferencia principal es que los string es una cadena de datos, la cual puede ser usada
en las listas, puesto que colectan distintos tipos de datos, así como string o enteros, 
también las listas pueden ser modificadas en el texto, mientras que los tuples no, esos son  
inalterables, y no se pueden modificar los datos, así como en los sets, tienen una condición
bastante curiosa puesto que los datos agregados serán arrojados de forma aleatoria y distinta  a
como lo habíamos escirto en un inicio, también teniendo la cualidad que los datos no se pueden 
repetir y solo se ven una única vez
"""

#Punto 3
text="I am a teacher and I love to inspire and teach people"
print(set(text.split()))


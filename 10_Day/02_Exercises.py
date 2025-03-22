#Punto 1
sum=0
for i in range (0,101):
    sum= sum + i
print("La suma de todos los números es: ",sum)

#Punto 2
even=0
odd=0
for i in range (0,101):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
print("La suma de todos los números pares es: ",even,". Y la suma de los números impares es: ",odd)


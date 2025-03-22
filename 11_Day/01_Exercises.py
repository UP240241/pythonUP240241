#Punto 1
def add_two_numbers(a,b):
    sum=a+b
    return sum
print(add_two_numbers(1,8))

#Punto 2
def area_of_circle(r):
    PI=3.14
    area= PI * r * r
    return area
print(area_of_circle(4))

#Punto 3
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num   
print(sum_all_nums(2, 3, 5)) 

#Punto 4
def convert_celsius_to_fahrenheit(C):
    F=(C * (9/5) +32)
    return F
print(convert_celsius_to_fahrenheit(35))

#Punto 5
def check_season(month):
    if month in ["Septiembre", "Octubre", "Noviembre"]:
        print("Otoño")
    if month in ["Diciembre", "Enero", "Febrero"]:
        print("Invierno")
    if month in ["Marzo", "Abril", "Mayo"]:
        print("Primavera")
    if month in ["Junio","Julio","Agosto"]:
        print("Verano")
print(check_season(input("Ingrese el mes: ")))

#Punto 6
def calculate_slope(x1,x2,y1,y2):
     m = (y2 - y1) / (x2 - x1)
     return m

print(calculate_slope(3,6,8,9))

#Punto 7
def solve_quadratic_eqn(a,b,c):
     D = b * b - 4 * a * c
     X1 = (-b + D) / (2 * a)
     return X1

print(solve_quadratic_eqn(8,4,6))

#Punto 8
def print_list(list):
    for i in list:
        print(i)
print(print_list)

#Punto 9
def reverse_list(a):
    return a[::-1]
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

#Punto 10
def capital_list_terms(a):
    for i in a:
        a[a.index(i)] = i.capitalize()
    return a

#Punto 11
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
def add_item (list,item):
    list.append(item)
    return list
print(add_item(food_staff, 'Meat')) 
print(add_item(numbers, 5))

#Punto 12
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]
def remove_item (list,item):
    list.remove(item)
    return list
print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3))

#Punto 13
def sum_of_numbers(number):
     sum_of_numbers = 0
     for i in range (number + 1):
        sum_of_numbers += i
     return sum_of_numbers
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Punto 14
def sum_of_odds (odd):
     sum_of_odd_nums = 0
     for i in range(odd + 1):
        if i % 2 == 1:
            sum_of_odd_nums += i
     return sum_of_odd_nums
print(sum_of_odds(10))

#Punto 15
def sum_of_even(even):
     sum_of_even_nums = 0
     for i in range(even + 1):
        if i % 2 == 1:
            sum_of_even_nums += i
     return sum_of_even_nums
print(sum_of_even(33))
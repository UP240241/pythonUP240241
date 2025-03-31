#Punto 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
number = [i for i in numbers if i <= 0]
print(number)

#Punto 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list=[i for sub in list_of_lists for sub2 in sub for i in sub2]
print(list)

#Punto 3
result = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)            

#Punto 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(output)

#Punto 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]
print(output)

#Punto 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [f"{first} {last}" for sublist in names for first, last in sublist]
print(output)

#Punto 7
linear_function = lambda x1, y1, x2, y2, calc: (y2 - y1) / (x2 - x1) if calc == 'slope' else y1 - ((y2 - y1) / (x2 - x1)) * x1
slope = linear_function(1, 2, 3, 6, 'slope')  
y_intercept = linear_function(1, 2, 3, 6, 'y-intercept') 

print("Slope:", slope)
print("Y-Intercept:", y_intercept)
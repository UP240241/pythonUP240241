#Punto 1
string1, string2, string3, string4="Thirty ", "Days ", "Of ","Python"
complete=string1 + string2 + string3 + string4
print(complete)

#Punto 2
string5, string6, string7 = "Coding ", "For ", "All"
complete1=string5 + string6 + string7
print(complete1)

#Punto 3
company="Coding For All"

#Punto 4
print(company)

#Punto 5
print(len(company))

#Punto 6
print(company.upper())

#Punto 7
print(company.lower())

#Punto 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Punto 9
slice=company[0:6]
print(slice)

#Punto 10
print(company.find("Coding"))

#Punto 11
print(company.replace("Coding", "Python"))

#Punto 12
print("Python for Everyone".replace("Everyone", "All"))

#Punto 13
print(company.split())

#Punto 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

#Punto 15
print(company[0])

#Punto 16
print(company[-1])

#Punto 17
print(company[10])

#Punto 18
#PFE="Python For Everyone"
words = "Python For Everyone".split()
print(words[0][0] + words[1][0] + words[2][0])

#Punto 19
words1="Coding For All".split()
print(words1[0][0] + words1[1][0] + words1[2][0])

#Punto 20
print(company.index("C"))

#Punto 21
print("Python For Everyone".index("F"))

#Punto 22
print("Coding for All People".rfind("l"))

#Punto 23
print('You cannot end a sentence with because because because is a conjunction'.find("because"))

#Punto 24
print('You cannot end a sentence with because because because is a conjunction'.rfind("because"))

#Punto 25
slice1='You cannot end a sentence with because because because is a conjunction'[31:55]
print(slice1)

#Punto 26
print('You cannot end a sentence with because because because is a conjunction'.index("because"))

#Punto 27
print(slice1)

#Punto 28
print(company.startswith("Coding"))

#Punto 29
print(company.endswith("coding"))

#Punto 30
c='   Coding For All      ' 
print(c.strip("   "))

#Punto 31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#Punto 32
v=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
value="#  ".join(v)
print(value)

#Punto 33
print("I am enjoying this challenge. \nI just wonder what is next. ")

#Punto 34
print("Name\t\tAge")
print("City\t\tCountry")
print("Asabeneh\t250")
print("Helsinki\tFinland")

#Punto 35
print("radius = {}".format(10))
print("area = {} * radius ** {}".format(3.14, 2))
print("The area of a circle with radius {} is {} meters square".format(10, 314))

#Punto 36
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

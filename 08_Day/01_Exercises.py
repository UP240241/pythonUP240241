#Punto 1
dog = dict()

#Punto 2
dog["name"] = "Pericles"
dog["color"] = "Verde"
dog["breed"] = "Pomeranian"
dog["legs"] = 4
dog["age"] = 1
print(dog)

#Punto 3
student={"first_name":"Magdalena",
"last_name":"Pérez",
"gender":"Mujer",
"age":20,
"marital_status":"Soltero",
"skills":["Bailar", "Matemáticas", "Análisis"],
"country":"España",
"city":"Madrid",
'address':{
'street':'Madrileño',
'zipcode':'02210'}}
print(student)
print(student.get("first_name"))

#Punto 4
print(len(student))

#Punto 5
print(student["skills"])
print(type(student["skills"]))

#Punto 6
student["skills"].append("Tecleo")
student["skills"].append("Programación")
print(student["skills"])

#Punto 7
list_keys = student.keys()
print(list_keys)

#Punto 8
list_values = student.values()
print(list_values)

#Punto 9
print(student.items())

#Punto 10
student.pop("address")

#Punto 11
del student
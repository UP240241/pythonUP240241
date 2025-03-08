#Punto 1
empty=list()
print(empty)

#Punto 2
list=["naranja", "piña","toronja", "papaya", "manzana"]
print(list)

#Punto 3
print(len(list))

#Punto 4
print(list[0])
print(list[2])
print(list[4])

#Punto 5
mixed_data_types=["Ismael",18,176,"Soltero","Aguascalientes"]

#Punto 6
it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

#Punto 7
print(it_companies)

#Punto 8
print(len(it_companies))

#Punto 9
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

#Punto 10
it_companies[2]="Instagram"
print(it_companies)

#Punto 11
it_companies.append("Alphabet")
print(it_companies)

#Punto 12
it_companies.insert(len(it_companies)//2, "Microsoft")
print(it_companies)

#Punto 13
it_companies1=it_companies[1].upper()
print(it_companies1)

#Punto 14
string=["#; "]
join = it_companies + string
print(join)

#Punto 15
does_exist= "Instagram" in it_companies
print(does_exist)

#Punto 16
it_companies.sort()
print(it_companies)

#Punto 17
it_companies.reverse()
print(it_companies)

#Punto 18
slice=it_companies[0:3]
print(slice)

#Punto 19
slicereverse=it_companies[-3:]
print(slicereverse)

#Punto 20
slicemiddle=it_companies[len(it_companies)//2]
print(slicemiddle)

#Punto 21
it_companies.pop(0)
print(it_companies)

#Punto 22
it_companies.pop(len(it_companies)//2)
print(it_companies)

#Punto 23
it_companies.pop()
print(it_companies)

#Punto 24
del it_companies[0:6]
print(it_companies)

#Punto 25
del it_companies

#Punto 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
end= front_end + back_end
print(end)

#Punto 27
full_stack=end.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)
#Punto 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#Punto 2
it_companies.add("Twitter")
print(it_companies)

#Punto 3
it_companies.update(["Instagram","Tesla","YouTube"])
print(it_companies)

#Punto 4
it_companies.remove("YouTube")
print(it_companies)

#Punto 5
""" Al usar Remove, busca el valor en el set, y si no lo encuentra
marca un error, sin embargo al usar Discard no marca ningún error aunque 
no se encuentre en el conjunto, por lo que si lo elimina o no, no marca nada."""

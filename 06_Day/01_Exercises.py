#Punto 1
empty=tuple()

#Punto 2
brothers=("Julian","Martín","Ulises","Andrés")
sisters=("María", "Martina", "Lucía","Olga")
print(brothers)
print(sisters)

#Punto 3
siblings= brothers + sisters
print(siblings)

#Punto 4
print(len(siblings))

#Punto 5
family_members=list(siblings)
family_members.append("Olimpo")
family_members.append("Liliana")
family_members=tuple(family_members)
print(family_members)
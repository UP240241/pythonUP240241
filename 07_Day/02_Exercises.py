#Variables
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Punto 1
C=A.union(B)
print(C)

#Punto 2
print(A.intersection(B))

#Punto 3
print(A.issubset(B))

#Punto 4
print(A.isdisjoint(B))

#Punto 5
print(A.union(B))
print(B.union(A))

#Punto 6
print(A.symmetric_difference(B))

#Punto 7
del A
del B
del C
#Punto 1
i=0
for i in range (11):
    print(i)
    i=i+1
i=0
while i <= 10:
    print(i)
    i=i+1

#Punto 2
for i in range(10, -1, -1):
    print(i)
i=10
while i >= 0:
    print(i)
    i=i-1

#Punto 3
hash="#"
i=1
for i in range(9):
    print(hash * i)
    i=i+1

#Punto 4
hash="# "
i=0
j=0
for i in range(9):
    for j in range(1):
        print(hash * 8)
        j=j+1
    i=i+1

#Punto 5
i=0
for i in range (11):
    print(i," X ",i," = ",i*i)
    i=i+1

#Punto 6
items=['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)

#Punto 7
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

#Punto 8
for i in range(0, 101):
    if i % 2 == 0:
        pass
    else:
        print(i)
#Punto 1
brothers=("Julian","Martín","Ulises","Andrés")
sisters=("María", "Martina", "Lucía","Olga")
siblings= brothers + sisters
family_members=list(siblings)
family_members.append("Olimpo")
family_members.append("Liliana")
family_members=tuple(family_members)
print(family_members)
*siblings, father, mother=family_members
print(siblings)
print(father)
print(mother)

#Punto 2
fruits=("apples","pineapple","watermelon","banana")
vegetables=("onion","tomatoe","carrots","cabagge")
animal_products=("milk","eggs","cheese","meat")
food_stuff_tp=fruits + vegetables + animal_products
print(food_stuff_tp)

#Punto 3
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

#Punto 4
print(food_stuff_lt[len(food_stuff_lt)//2])

#Punto 5
first_three=food_stuff_lt[0:3]
last_three=food_stuff_lt[-3:]
print(first_three)
print(last_three)

#Punto 6
food_stuff_tp=tuple(food_stuff_lt)
del food_stuff_tp

#Punto 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

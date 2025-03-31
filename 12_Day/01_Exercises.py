import random
import string
#Punto 1
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters, k=6))
    return user_id
print(random_user_id())

#Punto 2
ID= int(input("Cuántas ID quieres generar? "))
digits= int(input("Cuántos caracteres quieres en el ID? "))
def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits
    IDS = [''.join(random.choices(characters, k=digits)) for _ in range(ID)]
    return IDS
generated_ids = user_id_gen_by_user()
for gen in generated_ids:
    print(gen)

#Punto 3
def rgb_color_gen():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    return r,g,b
print(rgb_color_gen())
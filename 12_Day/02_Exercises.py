import random
import string
#Punto 1
def list_of_hexa_colors():
    hexa_colors = ['#' + ''.join(random.choices(string.hexdigits, k=6))]
    return hexa_colors
print(list_of_hexa_colors())

#Punto 2
def list_of_rgb_colors():
    rgb_colors = [(random.randint(0,255), random.randint(0,255), random.randint(0,255))]
    return rgb_colors
print(list_of_rgb_colors())

#Punto 3
cual=input("Qué tipo de color quieres generar? (Hexa o RGB) ")
num= int(input("Cuántos colores quieres generar? "))
if cual == "Hexa":
    def generate_colors():
        hexa_colors = ['#' + ''.join(random.choices(string.hexdigits, k=6)) for _ in range(num)]
        return hexa_colors
    print(generate_colors())
elif cual == "RGB":
    def generate_colors():
        rgb_colors = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for _ in range(num)]
        return rgb_colors
    print(generate_colors())

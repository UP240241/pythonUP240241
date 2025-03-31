import random
import string
#Punto 1
def shuffle_list(list):
    random.shuffle(list)
    return list
print(shuffle_list([1,2,3,4,5,6,7,8,9]))

#Punto 2
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())
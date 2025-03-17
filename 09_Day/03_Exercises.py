#Punto 1
person={
    'first_name': 'Ismael',
    'last_name': 'Reséndiz',
    'age': 18,
    'country': 'México',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Héroe de Nacozari',
        'zipcode': '20140'
    }
    }
if person['skills']:
    print(person['skills'][len(person['skills']) // 2])
    print("Python" in person["skills"])
if ["JavaScript","React"] == person["skills"]:
    print("He is a front end developer")
elif["Node","Python","MongoDB"] == person["skills"]:
    print("He is a backend developer")
elif["React","Node","MongoDB"] == person["skills"]:
    print("He is a fullstack developer")
else:
    print("Unknown title")
if person["is_married"] == True:
    if person["country"] == "Finland":
         print(person["first_name"], person["last_name"], "lives in",person["country"],"He is married")
    
else:
        print(person["first_name"], person["last_name"], "lives in",person["country"],"He is not married")
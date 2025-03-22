#Punto 1
def evens_and_odds (total):
    odds = 0
    evens = 0
    for i in range(total + 1):
        if i % 2 == 0:
            evens += i
        else:
            odds += i
    print(odds, evens)
print(evens_and_odds(100))

#Punto 2
def factorial(factorial):
     fact = 0
     for i in range(fact + 1):
        fact = fact * i
     return fact
print(factorial(3))

#Punto 3
def is_empty(check):
    if check == 0:
        return True
    else:
        return False
print(is_empty(1))

#Punto 4
numbers = [2, 3, 7, 9]
def calculate_mean(data):
    return sum(data) / len(data)
print(calculate_mean(numbers))

def calculate_median(data):
    data1 = sorted(data)
    index = len(data1) // 2

    if len(data) % 2 != 0:
        return data1[index]

    return (data1[index - 1] + data1[index]) / 2
print(calculate_median(numbers))

def calculate_mode(data):
    frequency = {}

    for value in data:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items() if value == most_frequent]

    return modes
print(calculate_mode(numbers))

def calculate_variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance
print(calculate_variance(numbers))

def calculate_std(data):
    var = calculate_variance(data)
    std_dev = var ** 0.5
    return std_dev
print(calculate_std(numbers))
import random

def f(list_name, list_otchestvo, list_family, n):
    i = 0
    while i < n:
        name = random.choice(list_name) + ' ' + random.choice(list_otchestvo) + ' ' + random.choice(list_family)
        i += 1
        yield name

for i in f(['Ivan', 'Sasha', 'Gosha'],['Ivanovich','Olegovich'],['Ivanov', 'Bobov'], 5):
    print(i)
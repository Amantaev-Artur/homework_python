import random

class Parent():
    def __init__(self, name, eyes, hair):
        self.name = name
        self.eyes = eyes
        self.hair = hair

class Child(Parent):
    def __init__(self,name, p1, p2):
        self.name = name
        list_1 = [p1.eyes, p2.eyes]
        list_2 = [p1.hair, p2.hair]
        self.eyes = random.choice(list_1)
        self.hair = random.choice(list_2) 

p1 = Parent('Biba', 'dark', 'blond')
p2 = Parent('Boba', 'blue', 'black')
c = Child('Buba', p1, p2)
print(p1.name)
print(p2.name)
print(c.name)
print(c.eyes)
print(c.hair)
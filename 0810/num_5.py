import string
import random
def generate_string(n):
    l = ''
    for i in range(n):
        l += (random.choice(string.ascii_letters))
    return l

def counter(l):
    small = 0
    big = 0
    for i in l:
        if i in string.ascii_lowercase:
            small += 1
        elif i in string.ascii_uppercase:
            big += 1
    if big > small:
        return 1
    elif big < small:
        return -1
    else: return 0

def function(list_1):
    kol_1 = 0
    kol_0 = 0
    for i in (list_1):
        q = counter(i)
        if q == 1:
            kol_1 += 1
        elif q == 0:
            kol_0 += 1
    print('Количество строк, в которых больше заглавных букв:',kol_1*100/len(list_1))
    print('Количество строк, в которых больше маленьких букв:',(len(list_1) - kol_1 - kol_0)*100/len(list_1))
    print('Количество строк, в которых одинаковое число заглавных и маленьких букв:',kol_0*100/len(list_1))

function([generate_string(5), generate_string(10), generate_string(45), generate_string(4), generate_string(10), generate_string(3), generate_string(47)])
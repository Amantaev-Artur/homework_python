def function(listA, a, n, char):
    switcher = {
        "center": "^",
        "left": "<",
        "right": ">"
    }
    arg = switcher.get(a)
    str = ""
    for i in listA:
            str += ('{0:'+ char + arg + '%s'%n + 's}').format(i)
            str += '\n'
    return str

print(function(['AAA','SSSSS','G'], 'center', 10, '!'))

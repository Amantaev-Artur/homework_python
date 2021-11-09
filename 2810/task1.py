import matplotlib.pyplot as plt
import numpy as np

a = ""
while (a != 'n'):
    xs = input('x: ')
    ys = input('y: ')
    color = input("Color: ")
    try:
        x = [int(x) for x in xs.split()]
        y = [int(y) for y in ys.split(' ')]
        if (color):
            plt.plot(x, y, color)
        else :
            plt.plot(x, y)    
    except Exception:
        print('Error')
    a = input('Введите n, если хотите закончить, или y, если хотите добавить еще график: ')

plt.show()
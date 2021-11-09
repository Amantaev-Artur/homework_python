import matplotlib.pyplot as plt
import numpy as np

def myBar(*args, **kwargs):
    try:
        x = args[0]
        y = args[1]
        barlist = plt.bar(x,y)
        for i in range(len(x)):
            color = 'color' + str(i)
            if color in kwargs:
                barlist[i].set_color(kwargs[color])
    except Exception as e:
        print(e)
    plt.show()

myBar(['A',"B",'C'], [5,10,15], color0='r', color2='g')
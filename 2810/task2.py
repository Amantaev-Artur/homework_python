import matplotlib.pyplot as plt
import numpy as np

def draw_plots(*args, **kwargs):
    i = 1
    for list_1 in args:
        x, y = list_1[0], list_1[1]
        try:
            color = 'color' + str(i)
            if (color in kwargs.keys()):
                plt.plot(x, y, color = kwargs[color])
            else:
                plt.plot(x, y)
        except Exception as e:
            print(e)
        i += 1
    plt.show()

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

x = [0,1,2,3]
y = [0,1,2,3]
x1 = [0,1,2,3]
y1 = [0,1,8,27]
draw_plots([x, y], [x1, y1], color1 = 'red')
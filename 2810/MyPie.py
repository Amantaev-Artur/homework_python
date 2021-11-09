import matplotlib.pyplot as plt
import numpy as np

def draw_pie(*args):
    sizes = []
    labels = []
    colors = []
    for size, label, color in args:
        sizes.append(size)
        labels.append(label)
        colors.append(color)
    plt.pie(sizes, colors = colors, startangle=90, autopct='%1.2f%%')
    plt.legend(labels, loc = 'best')
    plt.show()


draw_pie((12,'name1', 'red'), (20, 'name2', 'b'), (40, 'name3', 'green'), (20, 'name4', 'yellow'))
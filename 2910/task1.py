import numpy as np

def transponeM(list_1):
    npa = np.transpose(list_1)
    return npa.tolist()

def multiplyM(list_1, list_2):
    return np.dot(list_1, list_2).tolist()

def addM(list_1, list_2):
    return np.add(list_1, list_2).tolist()

def miniM(list_1, start1, end1, start2, end2):
    npa = np.reshape(list_1, (len(list_1), len(list_1[0])))
    npa = npa[start1:end1, start2:end2]
    return npa.tolist()

list1 = [[1,2,3],[4,5,6],[7,8,9]]
list2 = [[0,8,9],[5,6,7],[1,1,2]]
print(transponeM(list1))
print(multiplyM(list1, list2))
print(addM(list1, list2))
print(miniM(list1, 1,2,0,1))
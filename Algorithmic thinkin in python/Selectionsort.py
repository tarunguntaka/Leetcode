
import enum
from operator import le


def find_min(x):
    min_idx = 0
    for i in range(len(x)):
        if x[i] < x[min_idx]:
            min_idx = i 
    return x[min_idx]

def selection_sort(x):
    for i in range(len(x)):
        x1 = x[i::]
        min = find_min(x1)
        x[i] = min
    return x

a = selection_sort([2,9,3,8,4,5,6])
print(a)
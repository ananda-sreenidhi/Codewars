"""
Moving Zeros To The End
https://www.codewars.com/kata/52597aa56021e91c93000cb0
"""

def move_zeros(array):
    l = []
    s = 0
    for i in array: 
        if i!= 0 or type(i) == type(True):
            l.append(i)
        elif i == 0:
            s += 1
    for i in range(s):
        l.append(0)
    return l

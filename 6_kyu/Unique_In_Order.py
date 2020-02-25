"""
Unique In Order
https://www.codewars.com/kata/54e6533c92449cc251001667
"""

def unique_in_order(i):
    l = []
    l2 = []
    n = len(i)
    if n == 0:
        return []
    else:
        for j in i:
            l.append(j)
        l2.append(l[0])
        for x in l[1:]:
            if x != l2[len(l2)-1]:
                l2.append(x)  
        return l2

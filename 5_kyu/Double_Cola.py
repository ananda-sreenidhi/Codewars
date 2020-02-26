"""
Double Cola
https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0
"""

def whoIsNext(names, r):
    x, total = 0, 0
    while True:
        for name in names:
            total = (2 ** x) + total 
            if total >= r:
                return name 
        x += 1

"""
Distance between Black and White
https://www.codewars.com/kata/58e927c3cf8fff9296000108
"""

def distance(a,b):
    c = 0
    for i in range(len(a)):
        c += (a[i]-b[i]) **2
    return str(round(c**0.5, 2))

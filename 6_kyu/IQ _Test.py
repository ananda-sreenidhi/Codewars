"""
IQ Test
https://www.codewars.com/kata/552c028c030765286c00007d
"""

def iq_test(numbers):
    x = [int(i)%2 for i in numbers.split()]
    return x.index(1)+1 if sum(x) == 1 else x.index(0)+1

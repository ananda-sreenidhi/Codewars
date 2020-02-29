"""
Highest and Lowest
https://www.codewars.com/kata/554b4ac871d6813a03000035/
"""

def high_and_low(numbers):
    l = [int(i) for i in numbers.split(" ")]
    return "{} {}".format(max(l),min(l))

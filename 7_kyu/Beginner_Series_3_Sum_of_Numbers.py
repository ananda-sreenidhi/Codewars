"""
Beginner Series #3 Sum of Numbers
https://www.codewars.com/kata/55f2b110f61eb01779000053
"""

def get_sum(a,b):
    sum = 0
    if a==b:
        return a
    else:
        for i in range(min(a,b), max(a,b)+1):
            sum+=i
        return sum

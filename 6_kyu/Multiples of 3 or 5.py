"""
Multiples of 3 or 5
https://www.codewars.com/kata/514b92a657cdc65150000006
"""

def solution(number):
#returns sum of multiples of 3 and 5 in the range of given argument.
    if str(number).isdigit():
        l = range(number)
        return sum(filter(lambda x: x%3==0 or x%5==0, l))  

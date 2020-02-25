"""
Calculate average
https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
"""

def find_average(l):
    return sum(l)/len(l) if len(l)>0 else 0

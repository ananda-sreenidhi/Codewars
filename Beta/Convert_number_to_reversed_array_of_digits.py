"""
Convert number to reversed array of digits
https://www.codewars.com/kata/5583090cbe83f4fd8c000051
"""

def digitize(n):
    return [int(i) for i in list(str(n)[::-1])]

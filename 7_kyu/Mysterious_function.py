"""
Mysterious function
https://www.codewars.com/kata/55217af7ecb43366f8000f76
"""

def get_num(n):
    return sum([2 if i == '8' else 1 for i in str(n) if i in ('0','6','8','9')])

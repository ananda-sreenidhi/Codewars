"""
Mysterious function #1
https://www.codewars.com/kata/531963f82dde6fc8c800048a
"""

def solved(string):
    if len(string) % 2 == 1:
        return "".join(sorted(string[0:len(string)//2] + string[len(string)//2+1:]))
    else:
        return "".join(sorted(string))

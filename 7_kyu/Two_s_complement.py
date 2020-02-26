"""
Two's complement
https://www.codewars.com/kata/5874d1c9d5abe8e534000235
"""

def get_two_complement_int(n):
    l = list((str(bin(n))[2:])[::-1])
    d = {'0':'1', '1':'0'}
    l = [d[i] for i in l]
    return int('0b'+str(''.join(l))[::-1], 2)+1

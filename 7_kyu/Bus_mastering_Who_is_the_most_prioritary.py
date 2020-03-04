"""
Bus mastering - Who is the most prioritary?
https://www.codewars.com/kata/5a0366f12b651dbfa300000c
"""

def arbitrate(input, n):
    return '0'*input.find('1')+'1'+'0'*(len(input)-input.find('1')-1) if '1' in input else input

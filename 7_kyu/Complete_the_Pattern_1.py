"""
Complete the Pattern #1
https://www.codewars.com/kata/5572f7c346eb58ae9c000047
"""

def pattern(n):
    s = ""
    for i in range (1, n+1): s+=(str(i)*i) + '\n'
    return s.strip()

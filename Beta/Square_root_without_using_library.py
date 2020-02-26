"""
Square root without using library : math
https://www.codewars.com/kata/5979d27b630baf1509000064
"""

def square_root_me(sqrt):
    if sqrt == 0: return 0
    a = 0.5 * sqrt
    b = 0.5 * (a + sqrt/a)
    while b != a:
        a = b
        b = 0.5 * (a + sqrt/a)
    return a

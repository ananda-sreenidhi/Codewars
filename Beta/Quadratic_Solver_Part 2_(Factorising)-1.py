"""
Quadratic Solver Part 2 (Factorising)-1
https://www.codewars.com/kata/5894649d9521d7bf9600012b
"""

def solver(a, b, c):
    alpha = round((b-(b**2-4*a*c)**0.5)/(2*a), 1)
    beta = round((b+(b**2-4*a*c)**0.5)/(2*a), 1)
    return "(x{}{})(x{}{})".format('+' if alpha>=0 else '', alpha, '+' if beta>=0 else '', beta)

"""
Convert number to reversed array of digits
"""

def digitize(n):
    return [int(i) for i in list(str(n)[::-1])]

"""
Printer Errors (7kyu)
https://www.codewars.com/kata/56541980fa08ab47a0000040
"""

def printer_error(s):
    return "{}/{}".format(len([i for i in s.lower() if ord(i)>ord('m')]), len(s))

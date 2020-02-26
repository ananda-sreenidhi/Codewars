"""
Is this my tail?
https://www.codewars.com/kata/56f695399400f5d9ef000af5
"""

def correct_tail(body, tail):
    sub = body[len(body)-len(tail)]
    if sub == tail:
        return True
    return False

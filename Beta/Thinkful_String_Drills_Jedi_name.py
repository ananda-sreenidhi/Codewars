"""
Thinkful - String Drills: Jedi name
https://www.codewars.com/kata/585a29183d357b31f700023f
"""

def greet_jedi(first, last):
    return "Greetings, master {}{}".format(last[:3].capitalize(), first[:2].capitalize())

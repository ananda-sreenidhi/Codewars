"""
Greetings
https://www.codewars.com/kata/5901c9d463bf406d7c000107
"""

def greetings(time, name):
    return "Good {} {}".format(time, name) if time is not None else "Hey dude greet someone"

"""
All Star Code Challenge #9
https://www.codewars.com/kata/5864614683f7e6e7830000c1
"""

def bite(thing):
    if 'race' in thing and thing['race'] == 'human':
        thing['race'] = 'zombie'
    return thing

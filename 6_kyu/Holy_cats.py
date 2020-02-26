"""
Holy cats
https://www.codewars.com/kata/58ebfa6ef7cda1a3d4000048
"""

def holycats(cats):
    return [i for i in cats if not i[0].isalnum()]

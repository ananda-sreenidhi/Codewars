"""
Coding Meetup #17 - Higher-Order Functions Series - Sort by programming language
https://www.codewars.com/kata/583ea278c68d96a5fd000abd
"""

import operator
def sort_by_language(arr):
    arr.sort(key=operator.itemgetter('language', 'first_name'))
    return arr

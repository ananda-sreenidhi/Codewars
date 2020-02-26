"""
Highest Number in An Array
https://www.codewars.com/kata/597a458c1bec870d75000009
"""

def highest_num(nums):
    return sorted(nums)[-1] if len(nums)>0 else 0

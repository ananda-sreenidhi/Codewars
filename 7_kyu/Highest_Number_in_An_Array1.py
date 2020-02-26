"""
Highest Number in An Array
https://www.codewars.com/kata/597a458c1bec870d75000009
"""

def highest_num(nums):
    if len(nums) == 0: return 0
    m = nums[0]
    for i in nums[1:]:
        if i>m: m = i
    return m

"""
Fix string case
https://www.codewars.com/kata/5b180e9fedaa564a7000009a
"""

import re
def solve(s):
    return s.upper() if len(re.findall('[A-Z]', s)) > len(re.findall('[a-z]', s)) else s.lower()

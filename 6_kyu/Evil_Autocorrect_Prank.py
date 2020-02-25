"""
Evil Autocorrect Prank
https://www.codewars.com/kata/538ae2eb7a4ba8c99b000439
"""

import re
def autocorrect(input):
    return re.sub(r"\b(\W*)((Yo|yo)u+|u)(\W*)\b", r"\1your sister\4",input)

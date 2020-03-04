"""
Thinkful - String Drills: Poem formatter
https://www.codewars.com/kata/585af8f645376cda59000200e1a727000047
"""

def format_poem(poem):
    return '.\n'.join(poem.split('. ')).strip()

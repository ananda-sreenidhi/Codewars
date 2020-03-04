"""
Hello World - Without Strings
https://www.codewars.com/kata/584c7b1e2cb5e1a727000047
"""

def hello_world():
    return (chr(44)+chr(32)).join(str(hello_world.__name__).title().split(chr(95)))+chr(33)

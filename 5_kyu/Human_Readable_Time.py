"""
Human Readable Time
https://www.codewars.com/kata/52685f7382004e774f0001f7
"""

def make_readable(seconds):
    h, m, s = 0, 0, 0 
    s = seconds%60; seconds = seconds/60
    m = seconds%60; seconds = seconds/60
    h = seconds
    if s<10:
        s = '0'+str(s)
    if m<10:
        m = '0'+str(m)
    if h<10:
        h = '0'+str(h)
    return "{}:{}:{}".format(h, m, s)

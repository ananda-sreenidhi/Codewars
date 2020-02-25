"""
Number of People in the Bus
https://www.codewars.com/kata/5648b12ce68d9daa6b000099
"""

def number(bus_stops):
    inside = bus_stops[0][0]
    i = 1
    while i<len(bus_stops):
        inside += bus_stops[i][0] - bus_stops[i][1]
        i += 1
    return inside

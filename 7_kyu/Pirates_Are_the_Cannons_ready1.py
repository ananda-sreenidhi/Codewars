"""
Pirates!! Are the Cannons ready!??
https://www.codewars.com/kata/5748a883eb737cab000022a6
"""

def cannons_ready(gunners):
    flag = 0
    for i in gunners.keys():
        if gunners[i] == 'aye':
            flag+=1
    return 'Fire!' if flag == len(gunners) else 'Shiver me timbers!'

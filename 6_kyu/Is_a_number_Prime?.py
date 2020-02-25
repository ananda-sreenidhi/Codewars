"""
Is a number prime
https://www.codewars.com/kata/5262119038c0985a5b00029f
"""

def is_prime(num):
  if str(num) in '01'or num <= 1:
      return False
  for i in range(2,num):
      if num%i==0 or num == 0 or num == 1:
          return False
  else:
      return True

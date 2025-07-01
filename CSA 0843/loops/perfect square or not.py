# --------------------------------------------------
# Author : C DASARATH
# Question: to check if a given number is a perfect
#  square or not.
# --------------------------------------------------

# CODE:
from math import sqrt
n = int(input())
if n % sqrt(n) == 0:
  print("perfect sq")
else:
  print("NOT a perfect square")

# Input:
# 25

# Output:
# perfect sq
#
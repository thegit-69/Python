# --------------------------------------------------
# Author : C DASARATH
# Question: to find the roots of a quadratic equation.
# --------------------------------------------------

# CODE:
from math import sqrt
a = float(input())
b = float(input())
c = float(input())

try:
  d = sqrt(b*b - 4 * a * c)
  x1 =(-b + d ) / 2 * a
  x2 = (-b - d) / 2 * a
  print(f"x1 = {x1}\nx2 = {x2}")

except ValueError:
    print("Roots are imaginary for the given Quadratic equation")



# Input:
# 1
# 2
# -3

# Output:
# x1 = 1.0
# x2 = -3.0
#
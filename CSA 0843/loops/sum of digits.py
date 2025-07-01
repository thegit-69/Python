# --------------------------------------------------
# Author : C DASARATH
# Question: find the sum of digits in a number
# --------------------------------------------------

# CODE:
n = int(input(""))
sum = 0
while (n > 0):
  r =int(n % 10)
  sum = sum + r
  n = n / 10
print(sum)

# Input:
# N = 456

# Output:
# 15
#
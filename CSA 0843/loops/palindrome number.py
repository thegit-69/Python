# --------------------------------------------------
# Author : C DASARATH
# Question: check if a number is a palindrome or not.
# --------------------------------------------------

# CODE:
n = int(input(""))
ognum = n
rev = 0
while (n > 0):
  r = n % 10
  rev = (rev * 10) + r
  n = n // 10
if ognum == rev:
  print(f"{ognum} is a palindrome")
else:
  print(f"{ognum} is NOT a palindrome")

# Input:
# 121

# Output:
# 121 is a palindrome
#
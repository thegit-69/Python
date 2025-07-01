# --------------------------------------------------
# Author : C DASARATH
# Question: string is a palindrome or not.
# --------------------------------------------------

# CODE:
s = input("")
rev = s[::-1]
if s == rev:
  print(f"{s} is Palindrome")
else:
  print(f"{s} is NOT a palindrome")

# Input:
# malayalam

# Output:
# malayalam is Palindrome
#
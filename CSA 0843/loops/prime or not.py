# --------------------------------------------------
# Author : C DASARATH
# Question: to check if a given number is prime or not.
# --------------------------------------------------

# CODE:
n = int(input())
count = 0
for i in range(1,n + 1):
  if n % i == 0:
    count += 1
if count == 2:
  print(f"{n} is prime")
else:
  print(f"{n} is NOT a prime")

# Input:
# 5

# Output:
# 5 is prime
#
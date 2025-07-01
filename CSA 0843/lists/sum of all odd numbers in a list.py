# --------------------------------------------------
# Author : C DASARATH
# Question: to find the sum of all odd numbers in a list.
# --------------------------------------------------

# CODE:
l = [1,2,3,5]
sum = 0
for i in range(len(l)):
  if l[i] % 2 != 0:
    sum += l[i]
print(f"{sum} of all odd numbers")

# Input:
# NO INPUT directly RUN the code

# Output:
# 9 of all odd numbers
#
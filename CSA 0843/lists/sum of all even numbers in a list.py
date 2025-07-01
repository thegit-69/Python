# --------------------------------------------------
# Author : C DASARATH
# Question: to find the sum of all even numbers in a list.
# --------------------------------------------------

# CODE:
l = [2,4,6,1,5]
sum = 0
for i in range(0,len(l)):
  if l[i] % 2 == 0:
    sum += l[i]
print(f"{sum} of all even numbers")

# Input:
# NO INPUT directly RUN the code

# Output:
# 12 of all even numbers
#
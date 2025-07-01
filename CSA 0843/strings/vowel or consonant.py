# --------------------------------------------------
# Author : C DASARATH
# Question: Given char is vowel or consonant
# --------------------------------------------------

# CODE:
s = input()
l = s.lower()
for c in l:
    if c in ("a","e","i","o","u"):
        print(f"{c} is vowel")
    else:
        print(f"{c} is consonant")

# Input:
# MILK

# Output:
''' m is consonant
i is vowel
l is consonant
k is consonant'''
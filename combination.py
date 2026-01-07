'''This program takes a word and a number as input.
- First, it sorts the letters of the word so they are in alphabetical order.
- Then, it uses Python’s itertools.combinations to make all possible groups of letters.
- It prints every group starting from size 1 up to the number you gave.
For example, if you type:
HACK 2


the program will sort the letters into A C H K and then print:
- All single letters: A, C, H, K
- All two‑letter groups in alphabetical order: AC, AH, AK, CH, CK, HK
So the program helps you easily list combinations of letters in a neat, sorted way.
'''

from itertools import combinations

# Read input
s, k = input().split()
k = int(k)

# Sort the string to ensure lexicographic order
s = ''.join(sorted(s))

# Generate combinations of length 1 to k
for i in range(1, k+1):
    for combo in combinations(s, i):
        print(''.join(combo))
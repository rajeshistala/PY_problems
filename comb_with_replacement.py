'''In this program, you are given a string S and a number N.
Your task is to generate all possible combinations of length N from the characters of the string, allowing characters to repeat.

First, the characters in the string are sorted so the output appears in alphabetical order.
Then, combinations_with_replacement is used to create all valid combinations where:

The order does not matter (AB is the same as BA)

Repetition is allowed (AA is valid)

Each combination is returned as a tuple of characters. These characters are then joined into a string and printed line by line.

 Key Concepts for Beginners:

sorted(S) → arranges characters alphabetically

combinations_with_replacement(S, N) → creates combinations allowing repeats

''.join() → converts character tuples into strings

Loop → prints each result neatly'''

from itertools import combinations_with_replacement

S, N = input().split()
N = int(N)

S = sorted(S)

for comb in sorted(combinations_with_replacement(S,N)):
    print(''.join(comb))
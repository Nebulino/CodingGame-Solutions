Your program must read a list of integers from the standard input and remove the duplicates, the resulting list must only contain the first occurrences of each integer and should be written to the standard output.
INPUT:
Line 1: an integer N for the number of integers in the list.
N next lines: an integer X of the list.
OUTPUT:
The list of integers without duplicates, sorted in order of appearance.
CONSTRAINTS:
0 < N < 1000
-1000 < X < 1000
EXAMPLE:
Input
7
1
1
3
1
3
2
3
Output
1
3
2
-}

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
j = []
n = int(input())
for i in range(n):
    x = int(input())
    if x not in j:
        j.append(x)

for l in j:
    print(l)



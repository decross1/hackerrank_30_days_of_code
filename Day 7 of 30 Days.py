## Hackerrank: Day 7 of 30 Days of Code

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
print(' '.join(map(str, arr[::-1])))

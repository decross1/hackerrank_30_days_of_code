## Hackerrank: Day 6 of 30 Days of Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
from __future__ import print_function

word_count = int(raw_input())

while word_count > 0:
    word = raw_input()
    word_even = []
    word_odd = []
    for i, c in enumerate(word):
        if i % 2 == 0:
            word_even.append(c)
        else:
            word_odd.append(c)
    print((''.join(map(str, word_even))) + ' ' + (''.join(map(str, word_odd))))
    word_count -= 1
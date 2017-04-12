## Hackerrank: Day 5 of 30 Days of Code
#!/bin/python
import sys

n = int(raw_input().strip())
r = range(1, 11)
for each in r:
    print(str(n) + ' x ' + str(each) + ' = ' +  str(int(n * each)))
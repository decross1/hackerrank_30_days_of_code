## Hackerrank: Day 9 of 30 Days of Code
N = int(raw_input())
def factorial(N):
    if N == 1:
        return 1
    else:
        return N * factorial(N - 1)

print(factorial(N))
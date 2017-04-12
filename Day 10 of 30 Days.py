## Hackerrank: Day 10 of 30 Days of Code
num = 11


def p(num):
    i = 0
    while 2 ** i <= num:
        i += 1
    return i - 1


val = 2 ** p(num)
m = p(num)

digit = []
while val != 0 and len(digit) <= m:
    if num - val >= 0:
        num -= val
        digit.append(1)
    else:
        digit.append(0)
    val /= 2

print digit


def longRunOne(s):
    big = 0
    curr = 0
    for c in s:
        if c == 1:
            curr += 1
        else:
            if curr > big:
                big = curr
            curr = 0
    if curr > big:
        big = curr
    return big


longRunOne(digit)

arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

ans = - sys.maxsize

for i in range(4):
    for j in range(4):
        val = sum([arr[i][j + z] for z in range(3)] +
                  [arr[i + 2][j + z] for z in range(3)]) + arr[i + 1][j + 1]
        if val > ans:
            ans = val
print(ans)

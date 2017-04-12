## Hackerrank: Day 8 of 30 Days of Code
T = int(raw_input())
N = []
L = []

name_dict = dict()


def update_dict(N):
    for i, j in N:
        name_dict[i] = j


for each in xrange(T):
    N.append(map(str, raw_input().split()))

update_dict(N)


def test_cases(T):
    for a0 in xrange(T):
        L.append(str(raw_input()))


test_cases(T)

for each in L:
    if each in name_dict:
        print(each + '=' + name_dict[each])
    else:
        print('Not found')

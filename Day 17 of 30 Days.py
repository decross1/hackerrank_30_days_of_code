## Hackerrank: Day 17 of 30 days of Code
#Write your code here
class Calculator(object):
    def power(self, n, p):
        self.n = n
        self.p = p
        if (self.n < 0) or (self.p < 0):
            raise Exception("n and p should be non-negative")
        else:
            return self.n ** self.p

myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e

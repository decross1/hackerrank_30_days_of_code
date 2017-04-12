## Hackerrank: Day 15 of 30 Days of Code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print current.data,
            current = current.next


def insert(self, head, data):
    # Complete this method
    if (head == None):
        head = Node(data)
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = Node(data)
    return head


mylist = Solution()

T = int(input())

head = None

for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head);

a = 3

try:
    int(a)
    pass
except:
    print "Bad String"

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

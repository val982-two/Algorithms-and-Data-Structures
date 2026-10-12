from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def push_back(self, item):
        self.items.append(item)

    def push_front(self, item):
        self.items.appendleft(item)

    def pop_front(self):
        return self.items.popleft()

    def is_empty(self):
        return len(self.items) == 0

    def pop_back(self):
        return self.items.pop()

    def back(self):
        return self.items[-1]

    def front(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()


def goblin(arr):
    first = Deque()
    second = Deque()
    result = []

    def balance():
        if second.size() > first.size():
            first.push_back(second.pop_front())
        elif first.size() > second.size() + 1:
            second.push_front(first.pop_back())

    for cmd in arr:
        action = cmd[0]
        
        if action == '+':
            num = cmd[1]
            second.push_back(num)
            balance()
            
        elif action == '*':
            num = cmd[1]
            second.push_front(num)
            balance()
            
        elif action == '-':
            if not first.is_empty():
                result.append(first.pop_front())
                balance()
                
    for res in result:
        print(res)

n = int(input())
arr = []
for _ in range(n):
    a = input().split()
    if len(a) == 2:
        pri, num = a
        arr.append([pri, int(num)])
    else:
        arr.append(['-'])

goblin(arr)
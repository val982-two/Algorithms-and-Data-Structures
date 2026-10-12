class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def back(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def __str__(self):
        return ''.join([str(_) for _ in self.items])

def N(arr):
    return all(val == i + 1 for i, val in enumerate(arr))

def carriage(arr):
    stack = Stack()
    res = []
    i = 1
    for el in arr:
        if el != i:
            stack.push(el)
        else:
            res.append(el)
            i += 1
        while stack and stack.back() == i:
            res.append(stack.pop())
            i += 1 
    while not stack.is_empty():
        res.append(stack.pop())
    return N(res)

n = int(input())
arr = list(map(int, input().split()))

if carriage(arr): print('YES')
else: print('NO')


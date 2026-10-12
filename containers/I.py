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

arr = list(map(int, input().split()))
stack = Stack()

count = 0

for el in arr:
    while not stack.is_empty() and stack.back()[0] != el and stack.back()[1] >= 3:
        count += stack.pop()[1]

    if stack.is_empty():
        stack.push([el, 1])
    else:
        if stack.back()[0] == el:
            stack.push([el, stack.pop()[1] + 1])
        else:
            if stack.back()[1] >= 3:
                count += stack.pop()[1]
            stack.push([el, 1])
if not stack.is_empty() and stack.back()[1] >= 3:
    count += stack.pop()[1]
            
print(count)
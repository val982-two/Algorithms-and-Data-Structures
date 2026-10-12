class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            last = self.items.pop()
            return last

    def back(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def __str__(self):
        return ''.join([str(_) for _ in self.items])

s = Stack()

expr = input().split()

for el in expr:
    if el == '+':
        b = s.pop()
        s.push(s.pop() + b)
    elif el == '-':
        b = s.pop()
        s.push(s.pop() - b)
    elif el == '*':
        b = s.pop()
        s.push(s.pop() * b)
    else:
        s.push(int(el))

print(s)
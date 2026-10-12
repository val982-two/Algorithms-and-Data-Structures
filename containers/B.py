class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            self.items.pop()

    def back(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def __str__(self):
        return ' -> '.join([str(_) for _ in self.items])


stack = Stack()

a = input()

for el in a:
    if el == ')' and stack.back() == '(':
        stack.pop()
    elif el == ']' and stack.back() == '[':
        stack.pop()
    elif el == '}' and stack.back() == '{':
        stack.pop()
    else:
        stack.push(el)

if stack.size() == 0:
    print('yes')
else:
    print('no')
    
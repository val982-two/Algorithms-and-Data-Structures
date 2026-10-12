from sys import exit

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        cur_min = item if not self.items else min(item, self.items[-1][1])
        self.items.append((item, cur_min))

    def is_empty(self):
        return len(self.items) == 0

    def get_min(self):
        if not self.is_empty():
            return self.items[-1][1]
        return float('inf')

    def pop(self):
        if not self.is_empty():
            return self.items.pop()[0]

    def back(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def __str__(self):
        return ' '.join([str(_) for _ in self.items])

def win_min(arr, k):
    if not arr or k <= 0:
        return []

    stack_a = Stack() #добавление
    stack_b = Stack() #удаление
    res = []

    for i in range(k):
        stack_a.push(arr[i])
    
    #минимум первого окна
    res.append(min(stack_a.get_min(), stack_b.get_min()))

    for i in range(k, len(arr)):
        if stack_b.is_empty():
            while not stack_a.is_empty():
                stack_b.push(stack_a.pop())
        
        stack_b.pop()
        
        stack_a.push(arr[i])

        #текущий минимум
        cur_min = min(stack_a.get_min(), stack_b.get_min())
        res.append(cur_min)

    return res

n, k = list(map(int, input().split()))
arr = [int(_) for _ in input().split()]

for el in win_min(arr, k):
    print(el)




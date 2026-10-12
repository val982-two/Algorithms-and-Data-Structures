from collections import deque
import sys

class Deque:
    def __init__(self):
        self.items = deque()

    def push_back(self, item):
        self.items.append(item)

    def push_front(self, item):
        self.items.appendleft(item)

    def pop_front(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def pop_back(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def back(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def __str__(self):
        return ' '.join([str(_) for _ in self.items])


p_1 = list(map(int, input().split()))
p_2 = list(map(int, input().split()))

player_1 = Deque()
for el in p_1:
    player_1.push_back(el)

player_2 = Deque()
for el in p_2:
    player_2.push_back(el)

count = 0
is_botva = False

while player_1.size() > 0 and player_2.size() > 0:
    c1 = player_1.pop_front()
    c2 = player_2.pop_front()
    
    if c1 == 0 and c2 == 9:
        player_1.push_back(c1)
        player_1.push_back(c2)

    elif c1 == 9 and c2 == 0:
        player_2.push_back(c1)
        player_2.push_back(c2)
        
    elif c1 > c2:
        player_1.push_back(c1)
        player_1.push_back(c2)

    else:
        player_2.push_back(c1)
        player_2.push_back(c2)
        
    count += 1
    
    if count >= 10**6:
        print('botva')
        is_botva = True
        break

if not is_botva:
    if player_1.size() == 0:
        print('second', count)
    elif player_2.size() == 0:
        print('first', count)
import heapq
import sys


data = sys.stdin.read().split()

n = int(data[0])
a = [int(x) for x in data[1 : n + 1]]

heap = []
for i, pop in enumerate(a, start=1):
    wait_time = max(1000 - pop, 1)
    heapq.heappush(heap, (wait_time, i, pop))

current_time = 0
current_pos = 1

while heap:
    birth_time, pos, pop = heapq.heappop(heap)

    travel_time = abs(pos - current_pos)
    time_available = birth_time - current_time

    if time_available < travel_time:
        print(birth_time)
        break

    current_time = birth_time
    current_pos = pos

    new_pop = pop + 1
    next_wait = max(1000 - new_pop, 1)
    next_birth = current_time + next_wait
    heapq.heappush(heap, (next_birth, pos, new_pop))
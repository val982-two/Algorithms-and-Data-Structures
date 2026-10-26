import heapq

n = int(input())
data = list(map(int, input().split()))

heap = data
heapq.heapify(heap)

total = 0
while len(heap) > 1:
    s = heapq.heappop(heap) + heapq.heappop(heap)
    total += s*0.05
    heapq.heappush(heap, s)

print(f'{total:.2f}')

import heapq as hq

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
# n = 5
# data = [[13, 4], [15, 1], [11, 5], [12, 3], [10, 3]]

data.sort()

heap = []
hq.heapify(heap)
hq.heappush(heap, sum(data[0]))

for el in data[1:]:
    if heap[0] <= el[0]:
        hq.heappop(heap)
        hq.heappush(heap, sum(el))
    else:
        hq.heappush(heap, sum(el))
print(len(heap))
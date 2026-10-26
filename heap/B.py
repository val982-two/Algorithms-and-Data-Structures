class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shiftUp(self, i):
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2

    def shiftDown(self, i):
        while 2 * i <= self.size:
            j = self.idxmaxChild(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def idxmaxChild(self, i):
        if i * 2 + 1 > self.size: return 2 * i
        elif self.heap[2 * i] > self.heap[2 * i + 1]: return 2 * i
        return 2 * i + 1

    def Insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.shiftUp(self.size)

    def delmax(self):
        if self.size == 0: return None
        removed = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.size -= 1
        self.heap.pop()
        self.shiftDown(1)
        return removed

heap = MaxHeap()

n = int(input())
arr = list(map(int, input().split()))
for el in arr:
    heap.Insert(-el)

res = []
for _ in range(n):
    res.append(-1 * heap.delmax())

print(*res)

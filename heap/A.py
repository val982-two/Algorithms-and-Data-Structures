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
            j = self.IdxMaxChild(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def IdxMaxChild(self, i):
        if i * 2 + 1 > self.size: return 2 * i
        elif self.heap[2 * i] > self.heap[2 * i + 1]: return 2 * i
        return 2 * i + 1

    def Insert(self, k):
        self.heap.append(k)
        self.size += 1
        self.shiftUp(self.size)

    def Extract(self):
        if self.size == 0: return None
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        maxn = self.heap.pop()
        self.size -= 1
        self.shiftDown(1)
        return maxn

heap = MaxHeap()

n = int(input())
inp = []
for _ in range(n):
    inp.append(list(map(int, input().split())))

out = []
for oper in inp:
    if len(oper) > 1:
        heap.Insert(oper[1])
    else:
        out.append(heap.Extract())
for el in out:
    print(el)
    
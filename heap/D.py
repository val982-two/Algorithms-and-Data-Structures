import sys


class MaxHeap:
  def __init__(self):
    self.heap = [0]
    self.size = 0

  def shiftUp(self, i):
    h = self.heap
    while i > 1:
      p = i // 2
      if h[i] > h[p]:
        h[i], h[p] = h[p], h[i]
        i = p
      else:
        break

  def shiftDown(self, i):
    h = self.heap
    sz = self.size
    while 2 * i <= sz:
      c = 2 * i
      if c + 1 <= sz and h[c + 1] > h[c]:
        c += 1
      if h[i] < h[c]:
        h[i], h[c] = h[c], h[i]
        i = c
      else:
        break

  def Insert(self, k):
    self.heap.append(k)
    self.size += 1
    self.shiftUp(self.size)

  def delmax(self):
    if self.size == 0:
      return "CANNOT"
    h = self.heap
    removed = h[1]
    h[1] = h[self.size]
    self.size -= 1
    h.pop()
    self.shiftDown(1)
    return str(removed)

  def Clear(self):
    self.heap = [0]
    self.size = 0


def main():
  heap = MaxHeap()
  output = []

  for line in sys.stdin:
    oper = line.split()
    if not oper:
      continue

    cmd = oper[0]
    if cmd == "ADD":
      heap.Insert(int(oper[1]))
    elif cmd == "EXTRACT":
      output.append(heap.delmax())
    elif cmd == "CLEAR":
      heap.Clear()

  if output:
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
  main()
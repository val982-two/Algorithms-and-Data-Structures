import sys


class Deque:
    def __init__(self):
        self.items = []

    def push_back(self, item):
        self.items.append(item)
        print("ok")

    def push_front(self, item):
            self.items.insert(0, item)
            print("ok")

    def is_empty(self):
        return len(self.items) == 0

    def pop_front(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items.pop(0))

    def pop_back(self):
            if self.is_empty():
                print("error")
            else:
                print(self.items.pop())

    def back(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[-1])

    def front(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[0])

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items.clear()
        print("ok")


def main():
    deque = Deque()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        command = parts[0]

        if command == "push_back":
            deque.push_back(parts[1])
        elif command == "push_front":
            deque.push_front(parts[1])
        elif command == "pop_front":
            deque.pop_front()
        elif command == "pop_back":
            deque.pop_back()
        elif command == "back":
            deque.back()
        elif command == "front":
            deque.front()
        elif command == "size":
            deque.size()
        elif command == "clear":
            deque.clear()
        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    main()
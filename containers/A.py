import sys


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print("ok")

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items.pop())

    def back(self):
        if self.is_empty():
            print("error")
        else:
            print(self.items[-1])

    def size(self):
        print(len(self.items))

    def clear(self):
        self.items.clear()
        print("ok")


def main():
    stack = Stack()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        command = parts[0]

        if command == "push":
            stack.push(parts[1])
        elif command == "pop":
            stack.pop()
        elif command == "back":
            stack.back()
        elif command == "size":
            stack.size()
        elif command == "clear":
            stack.clear()
        elif command == "exit":
            print("bye")
            break


if __name__ == "__main__":
    main()
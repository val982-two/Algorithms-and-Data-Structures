import sys
from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a: return -1
    elif a + b < b + a: return 1
    else: return 0

data = sys.stdin.read()
numbers = [_ for _ in data.split()]

numbers.sort(key=cmp_to_key(compare))

print(''.join(numbers))
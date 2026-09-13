import sys

def generate_anti_quicksort(n):
    a = list(range(1, n + 1))

    for i in range(2, n):
        pivot_index = i // 2
        a[i], a[pivot_index] = a[pivot_index], a[i]
        
    return a

n = int(input())

print(*(generate_anti_quicksort(n)))
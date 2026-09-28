n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

first = 0
last = 0
out = []

for el in m_arr:
    left = -1
    right = len(n_arr)

    while right - left > 1:
        mid = left + (right - left) // 2
        if el < n_arr[mid]:
            right = mid
        else:
            left = mid
    last = left

    left = -1
    right = len(n_arr)

    while right - left > 1:
        mid = left + (right - left) // 2
        if el <= n_arr[mid]:
            right = mid
        else:
            left = mid
    first = right

    out.append(last - first + 1)

for el in out:
    print(el, end=' ')

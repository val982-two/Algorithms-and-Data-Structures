def good(d, n, a, b, w, h):
    count_w1 = w // (a + 2 * d)
    count_h1 = h // (b + 2 * d)
    res1 = count_w1 * count_h1

    count_w2 = w // (b + 2 * d)
    count_h2 = h // (a + 2 * d)
    res2 = count_w2 * count_h2

    return res1 >= n or res2 >= n

n, a, b, w, h = list(map(int, input().split()))

left = 0
right = 2*10**18

while right - left > 1:
    mid = left + (right - left) // 2
    if good(mid, n, a, b, w, h):
        left = mid
    else:
        right = mid
print(left)
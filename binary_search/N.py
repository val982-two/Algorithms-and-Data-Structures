def trees_removed(day, a, k, b, m):
    rest_days_1 = day // k if k != 0 else 0
    
    rest_days_2 = day // m if m != 0 else 0
    
    total_trees = (day * a - rest_days_1 * a) + (day * b - rest_days_2 * b)
    
    return total_trees

A, K, B, M, X = list(map(int, input().split()))

left = -1
right = 2 * 10**18

while right - left > 1:
    mid = left + (right - left) // 2
    if trees_removed(mid, A, K, B, M) >= X:
        right = mid
    else:
        left = mid
print(right)
    
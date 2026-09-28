import sys

def get_balls(t, T, Z, Y):
    full_cycles = t // (Z * T + Y)
    remainder_time = t % (Z * T + Y)
    return full_cycles * Z + min(Z, remainder_time // T)


def check(t, M, helpers):
    total = 0
    for T, Z, Y in helpers:
        total += get_balls(t, T, Z, Y)
    return total >= M



M, N = map(int, input().split())
helpers = []
for _ in range(N):
    T, Z, Y = map(int, input().split())
    helpers.append((T, Z, Y))

if M == 0:
    print(0)
    print(*(0 for _ in range(N)))
    sys.exit(0)

left = 0
right = 10**9

while right - left > 1:
    mid = (left + right) // 2
    if check(mid, M, helpers):
        right = mid
    else:
        left = mid

print(right)

ans = []
balls_left = M

for T, Z, Y in helpers:
    can_inflate = get_balls(right, T, Z, Y)
    take = min(can_inflate, balls_left)
    ans.append(take)
    balls_left -= take

print(*ans)
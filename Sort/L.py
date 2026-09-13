def taxi(km, pr):
    sm = 0
    for _ in range(len(km)):
        sm += max(km) * min(pr)
        km.remove((max(km)))
        pr.remove((min(pr)))
    return sm

km = list(map(int, input().split()))
pr = list(map(int, input().split()))

print(taxi(km, pr))
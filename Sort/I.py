def anagram(w1: str, w2: str):
    if len(w1) != len(w2):
        return print('NO')

    counts = [0] * 256

    for i in range(len(w1)):
        counts[ord(w1[i])] += 1
        counts[ord(w2[i])] -= 1

    if all(x == 0 for x in counts): print('YES')
    else: print('NO')

w1 = input()
w2 = input()

anagram(w1, w2)


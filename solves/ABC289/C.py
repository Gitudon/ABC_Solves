N, M = map(int, input().split())
C = [0] * M
a = [0] * M
for i in range(M):
    C[i] = int(input())
    a[i] = list(map(int, input().split()))

mokuteki = [i for i in range(1, N + 1)]

ans = 0


def bit_all_search(current_set, now):
    global ans
    if now == M:
        if sorted(list(current_set)) == mokuteki:
            ans += 1
        return
    next_set = current_set.copy()
    bit_all_search(next_set, now + 1)
    for elem in a[now]:
        next_set.add(elem)
    bit_all_search(next_set, now + 1)


bit_all_search(set(), 0)
print(ans)

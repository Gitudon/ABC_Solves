N, K, M = map(int, input().split())
values_per_color = [0] * N
values_dict = {}
for _ in range(N):
    C, V = map(int, input().split())
    C -= 1
    if V in values_dict:
        values_dict[V] += 1
    else:
        values_dict[V] = 1
    values_per_color[C] = max(values_per_color[C], V)

values_per_color = sorted(values_per_color, reverse=True)[:M]

for v in values_per_color:
    values_dict[v] -= 1

ans = sum(values_per_color)
v_keys = sorted(values_dict.keys(), reverse=True)
res = K - M
j = 0
while res > 0:
    if values_dict[v_keys[j]] == 0:
        j += 1
    else:
        if res < values_dict[v_keys[j]]:
            ans += res * v_keys[j]
            res = 0
        else:
            ans += values_dict[v_keys[j]] * v_keys[j]
            res -= values_dict[v_keys[j]]
            j += 1

print(ans)

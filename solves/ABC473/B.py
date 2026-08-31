N = int(input())
A = list(map(int, input().split()))

a_dict = {}
for a in A:
    if a in a_dict:
        a_dict[a] += 1
    else:
        a_dict[a] = 1

ans = 0
for a in a_dict:
    if a_dict[a] % 2 == 1:
        ans += a

print(ans)

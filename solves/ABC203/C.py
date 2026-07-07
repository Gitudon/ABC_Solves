N, K = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

friends = {}
for i in range(N):
    if A[i] not in friends:
        friends[A[i]] = B[i]
    else:
        friends[A[i]] += B[i]

mura = sorted(friends.keys())

i = 0
current = 0
shojikin = K
max_i = len(mura)
while shojikin > 0:
    if i >= max_i:
        current += shojikin
        shojikin = 0
    else:
        if (mura[i] - current) <= shojikin:
            shojikin -= mura[i] - current
            shojikin += friends[mura[i]]
            current = mura[i]
            i += 1
        else:
            current += shojikin
            shojikin = 0

print(current)

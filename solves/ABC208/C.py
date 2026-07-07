N, K = map(int, input().split())
a = list(map(int, input().split()))

kokumin_dict = {}
for i in range(N):
    kokumin_dict[a[i]] = i

a = sorted(a)

sho = K // N
K_dash = K % N

okashi = [sho] * N
for i in range(K_dash):
    okashi[kokumin_dict[a[i]]] += 1

for i in range(N):
    print(okashi[i])

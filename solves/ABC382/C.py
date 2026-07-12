N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
buf_size = 200001
hash_hyo = [-1] * buf_size
for i in range(N):
    if hash_hyo[A[i]] == -1:
        hash_hyo[A[i]] = i + 1
last_value = -1
for k in range(buf_size):
    if hash_hyo[k] != -1:
        if last_value == -1:
            last_value = hash_hyo[k]
        else:
            if last_value > hash_hyo[k]:
                last_value = hash_hyo[k]
            else:
                hash_hyo[k] = last_value
    else:
        hash_hyo[k] = last_value
for j in range(M):
    print(hash_hyo[B[j]])

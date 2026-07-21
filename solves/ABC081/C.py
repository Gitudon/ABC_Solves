N, K = map(int, input().split())
A = list(map(int, input().split()))

dictionary = {}
for i in range(N):
    if A[i] in dictionary:
        dictionary[A[i]] += 1
    else:
        dictionary[A[i]] = 1

syurui = len(dictionary)
if syurui <= K:
    print(0)
else:
    ans = 0
    sorted_values = sorted(dictionary.values())
    for i in range(syurui - K):
        ans += sorted_values[i]
    print(ans)

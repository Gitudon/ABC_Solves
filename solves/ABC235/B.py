N = int(input())
H = list(map(int, input().split()))

i = 0
while i != N - 1:
    if H[i + 1] > H[i]:
        i += 1
    else:
        break
print(H[i])

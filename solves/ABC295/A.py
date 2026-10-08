N = int(input())
ans = 0
a = ["and", "not", "that", "the", "you"]
W = list(map(str, input().split()))
for i in range(N):
    if W[i] in a:
        print("Yes")
        exit()
print("No")

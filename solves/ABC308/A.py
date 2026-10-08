S = list(map(int, input().split()))
if sorted(S) != S:
    print("No")
    exit()
if max(S) > 675:
    print("No")
    exit()
if min(S) < 100:
    print("No")
    exit()
for i in range(8):
    if S[i] % 25 != 0:
        print("No")
        exit()
print("Yes")

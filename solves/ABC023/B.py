N = int(input())
S = input()

ans = "b"
tejun = 0

while len(ans) < N:
    tejun += 1
    if tejun % 3 == 1:
        ans = "a" + ans + "c"
    elif tejun % 3 == 2:
        ans = "c" + ans + "a"
    else:
        ans = "b" + ans + "b"

if ans == S:
    print(tejun)
else:
    print(-1)

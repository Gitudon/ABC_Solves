A, B = map(int, input().split())
ans = B // A + 1
if B % A == 0:
    ans -= 1
print(ans)

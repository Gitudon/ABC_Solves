A, B, C, K = map(int, input().split())

ans = 0
current = K

if current <= A:
    ans += current
    current = 0
else:
    ans += A
    current -= A

if current <= B:
    current = 0
else:
    current -= B

if current <= C:
    ans -= current
    current = 0
else:
    ans -= C
    current -= C

print(ans)

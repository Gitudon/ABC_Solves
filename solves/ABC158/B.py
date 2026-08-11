N, A, B = map(int, input().split())

foo = A + B
bar = N // foo
ans = A * bar

N %= foo

if N >= A:
    ans += A
else:
    ans += N

print(ans)

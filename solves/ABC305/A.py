N = int(input())
a = N // 5
b = 5 * a
c = 5 * (a + 1)
if abs(N - b) >= abs(N - c):
    print(c)
else:
    print(b)

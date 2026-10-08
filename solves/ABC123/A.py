a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())


def choku(x, k):
    if x > k:
        return 1
    else:
        return 0


f = 0
f += choku(e - a, k)
f += choku(d - a, k)
f += choku(c - a, k)
f += choku(b - a, k)
f += choku(e - b, k)
f += choku(d - b, k)
f += choku(c - b, k)
f += choku(e - c, k)
f += choku(d - c, k)
f += choku(e - d, k)

if f == 0:
    print("Yay!")
else:
    print(":(")

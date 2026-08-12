N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

foo = [a] + P + [b]
bar = list(set(foo))

if len(foo) == len(bar):
    print("YES")
else:
    print("NO")

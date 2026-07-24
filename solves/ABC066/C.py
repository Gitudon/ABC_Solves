n = int(input())
a = list(map(int, input().split()))

b = []
a_odd = []
a_even = []
for i in range(n):
    if i % 2 == 0:
        a_odd.append(a[i])
    else:
        a_even.append(a[i])

if n % 2 == 0:
    for i in range(1, len(a_even) + 1):
        b.append(a_even[-i])
    print(*(b + a_odd))
else:
    for i in range(1, len(a_odd) + 1):
        b.append(a_odd[-i])
    print(*(b + a_even))

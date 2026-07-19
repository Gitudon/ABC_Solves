N = int(input())
A = list(map(int, input().split()))

even = []
odd = []
for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)

even.sort()
odd.sort()

if len(even) == 0:
    print(odd[-1] + odd[-2])
elif len(odd) == 0:
    print(even[-1] + even[-2])
else:
    if len(even) == 1:
        if len(odd) == 1:
            print(-1)
        else:
            print(odd[-1] + odd[-2])
    else:
        if len(odd) == 1:
            print(even[-1] + even[-2])
        else:
            print(max(even[-1] + even[-2], odd[-1] + odd[-2]))

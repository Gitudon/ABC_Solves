l1, l2, l3 = map(int, input().split())
two = l1 + l2 + l3 - max(l1, l2, l3) - min(l1, l2, l3)
if two != l1:
    print(l1)
elif two != l2:
    print(l2)
else:
    print(l3)

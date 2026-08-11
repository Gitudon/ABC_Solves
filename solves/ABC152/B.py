a, b = map(int, input().split())

foo = str(a) * b
bar = str(b) * a

if foo < bar:
    print(foo)
else:
    print(bar)

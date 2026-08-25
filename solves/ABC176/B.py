N = input()

foo = 0
for i in range(len(N)):
    foo += int(N[i])

if foo % 9 == 0:
    print("Yes")
else:
    print("No")

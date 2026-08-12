A = list(map(int, input().split()))

kiroku = [0] * 14

for i in range(7):
    kiroku[A[i]] += 1

res = max(kiroku)

if res == 3:
    if 2 in kiroku:
        print("Yes")
    else:
        count = 0
        for i in range(14):
            if kiroku[i] == 3:
                count += 1
        if count == 2:
            print("Yes")
        else:
            print("No")
elif res == 4:
    if 2 in kiroku or 3 in kiroku:
        print("Yes")
    else:
        print("No")
elif res == 5:
    if 2 in kiroku:
        print("Yes")
    else:
        print("No")
else:
    print("No")

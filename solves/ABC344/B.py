A = []
while True:
    a = int(input())
    A.append(a)
    if a == 0:
        break
for i in range(1, len(A) + 1):
    print(A[-i])

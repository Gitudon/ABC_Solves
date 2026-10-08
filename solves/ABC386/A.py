A, B, C, D = map(int, input().split())
kiroku = [0] * 14
kiroku[A] += 1
kiroku[B] += 1
kiroku[C] += 1
kiroku[D] += 1
kazu = 0
for i in range(14):
    if kiroku[i] > 0:
        kazu += 1
saidaichi = max(kiroku)
if saidaichi == 3 or (saidaichi == 2 and kazu == 2):
    print("Yes")
else:
    print("No")

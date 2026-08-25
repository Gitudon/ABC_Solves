N = int(input())
S = [0] * N
for i in range(N):
    S[i] = input()
for i in range(N):
    for j in range(N):
        if i != j:
            T = S[i] + S[j]
            t = True
            for k in range(len(T)):
                if T[k] != T[len(T) - k - 1]:
                    t = False
                    break
            if t:
                print("Yes")
                exit()
print("No")

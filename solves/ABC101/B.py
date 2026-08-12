N = int(input())

S_N = 0
N_str = str(N)
for i in range(len(N_str)):
    S_N += int(N_str[i])

if N % S_N == 0:
    print("Yes")
else:
    print("No")

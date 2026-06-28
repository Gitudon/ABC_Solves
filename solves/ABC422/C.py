T = int(input())
for _ in range(T):
    n_A, n_B, n_C = map(int, input().split())
    print(min(n_A, n_C, int((n_A + n_B + n_C) / 3)))

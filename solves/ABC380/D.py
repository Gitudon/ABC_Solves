S = input()
Q = int(input())
K = list(map(int, input().split()))


def solve(k, l):
    if l == 0:
        return S[k - 1]
    h = len(S) * (2 ** (l - 1))
    if k <= h:
        return solve(k, l - 1)
    return chr(ord(solve(k - h, l - 1)) ^ 32)


# ^32 とするとASCII文字コードで大文字と小文字を変換できる

for k in K:
    print(solve(k, 60), end=" ")

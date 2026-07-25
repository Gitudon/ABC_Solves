from math import factorial

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


def index_of_permutation(L):
    index = 0
    while len(L) > 1:
        a = len([l for l in L if l < L[0]])
        index = index + a * factorial(len(L) - 1)
        L = L[1:]
    return index


ans = index_of_permutation(Q) - index_of_permutation(P) - 1
if ans < 0:
    ans = 0
print(ans)

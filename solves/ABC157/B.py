A = [list(map(int, input().split())) for _ in range(3)]

N = int(input())
card = [[False] * 3 for _ in range(3)]
ans = "No"


def check(card):
    for i in range(3):
        if all(card[i]):
            return True
    for j in range(3):
        if all(card[k][j] for k in range(3)):
            return True
    if all(card[i][i] for i in range(3)):
        return True
    if all(card[i][2 - i] for i in range(3)):
        return True
    return False


for i in range(N):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if A[j][k] == b:
                card[j][k] = True
    if check(card):
        ans = "Yes"
print(ans)

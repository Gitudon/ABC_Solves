k = int(input())
answer = []


def solve(x):
    if x > 3234566667:
        return
    answer.append(x)
    for i in range(10):
        if abs(i - x % 10) <= 1:
            solve(x * 10 + i)


for i in range(1, 10):
    solve(i)
answer = sorted(answer)
print(answer[k - 1])

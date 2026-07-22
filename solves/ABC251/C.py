N = int(input())
original = {}
scores = {}
max_score = 0
for i in range(N):
    S, T = map(str, input().split())
    if S not in original:
        original[S] = i + 1
        if T not in scores:
            scores[T] = []
        scores[T].append(original[S])
        max_score = max(max_score, int(T))

print(sorted(scores[str(max_score)])[0])

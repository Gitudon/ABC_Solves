N = int(input())

dictionary = {}
for _ in range(N):
    S = input().lower()
    if S in dictionary:
        dictionary[S] += 1
    else:
        dictionary[S] = 1

print(max(dictionary.values()))

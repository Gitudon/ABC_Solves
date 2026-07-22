N = int(input())

dictionary = {}
for _ in range(N):
    S = input()
    if S in dictionary:
        dictionary[S] += 1
    else:
        dictionary[S] = 1

max_count = max(dictionary.values())
ans = []
for key in dictionary:
    if dictionary[key] == max_count:
        ans.append(key)
ans.sort()
for a in ans:
    print(a)

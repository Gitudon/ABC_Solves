N = int(input())
dictionary = {}

for i in range(N):
    S = input()
    if S in dictionary:
        dictionary[S] += 1
    else:
        dictionary[S] = 1
max_value = max(dictionary.values())
for key in dictionary.keys():
    if dictionary[key] == max_value:
        print(key)

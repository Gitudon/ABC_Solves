S = input()

dic = {}
for s in S:
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

for key in dic:
    if dic[key] == 1:
        print(key)

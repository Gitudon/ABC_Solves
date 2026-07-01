N = int(input())
S = input()
memory = []
count = 0
for i in range(N):
    if S[i] == "-":
        memory.append(count)
        memory.append(0)
        count = 0
    if S[i] == "o":
        count += 1
        if i == N - 1:
            memory.append(count)
if len(memory) == 0 or 0 not in memory:
    ans = 0
else:
    ans = max(memory)
if ans == 0:
    print(-1)
else:
    print(ans)

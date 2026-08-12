from itertools import permutations

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

menus = [A, B, C, D, E]
all_permutations = list(permutations(menus))

ans = 10**10

for perm in all_permutations:
    time = 0
    for i in range(5):
        time += perm[i]
        foo = time % 10
        if i != 4:
            time += (10 - (foo)) % 10
    ans = min(ans, time)
print(ans)

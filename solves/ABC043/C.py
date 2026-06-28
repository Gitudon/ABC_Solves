N = int(input())
a = list(map(int, input().split()))

heikin_kirisage = sum(a) // N
heikin_kiriage = heikin_kirisage + 1
ans_one = 0
for i in a:
    ans_one += (i - heikin_kirisage) ** 2
ans_two = 0
for i in a:
    ans_two += (i - heikin_kiriage) ** 2
print(min(ans_one, ans_two))

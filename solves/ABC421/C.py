N = int(input())
S = list(input())
count = 0
i = 0

mohan_a = ["A", "B"] * N
a_to_b_miss = []
b_to_a_miss = []
for i in range(2 * N):
    if S[i] != mohan_a[i]:
        if S[i] == "A":
            a_to_b_miss.append(i)
        else:
            b_to_a_miss.append(i)
cnt_a = 0
for i in range(len(a_to_b_miss)):
    cnt_a += abs(a_to_b_miss[i] - b_to_a_miss[i])
mohan_b = ["B", "A"] * N
a_to_b_miss = []
b_to_a_miss = []
for i in range(2 * N):
    if S[i] != mohan_b[i]:
        if S[i] == "A":
            a_to_b_miss.append(i)
        else:
            b_to_a_miss.append(i)
cnt_b = 0
for i in range(len(a_to_b_miss)):
    cnt_b += abs(a_to_b_miss[i] - b_to_a_miss[i])
print(min(cnt_a, cnt_b))

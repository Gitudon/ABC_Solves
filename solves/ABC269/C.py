N = int(input())

ans = []
bin_N = bin(N)[2:][::-1]
one_idxs = []
for i in range(len(bin_N)):
    if bin_N[i] == "1":
        one_idxs.append(i)
max_num = len(one_idxs)


def bit_all_search(num, current):
    if num == max_num:
        ans.append(current)
        return
    bit_all_search(num + 1, current + 2 ** (one_idxs[num]))
    bit_all_search(num + 1, current)


bit_all_search(0, 0)
ans.sort()
for a in ans:
    print(a)

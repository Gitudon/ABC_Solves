N = int(input())
S = input()

one_num = S.count("1")

if one_num == 0 or one_num == N:
    print(0)
else:
    one_positions = [i for i, char in enumerate(S) if char == "1"]
    min_swaps = float("inf")
    for i in range(len(one_positions) - one_num + 1):
        mid = i + one_num // 2
        swaps = 0
        for j in range(one_num):
            swaps += abs(one_positions[i + j] - (one_positions[mid] - one_num // 2 + j))
        min_swaps = min(min_swaps, swaps)
    print(min_swaps)

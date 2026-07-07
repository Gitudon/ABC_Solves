H, W, K = map(int, input().split())
c = [input() for _ in range(H)]

ans = 0


def count_black(exclude_row, exclude_column):
    count = 0
    for i in range(H):
        if i in exclude_row:
            continue
        for j in range(W):
            if j in exclude_column:
                continue
            if c[i][j] == "#":
                count += 1
    return count


def bit_all_search(now_exclude_row, now_exclude_column, count):
    global ans
    if count == H + W:
        if count_black(now_exclude_row, now_exclude_column) == K:
            ans += 1
        return
    if count < H:
        bit_all_search(now_exclude_row + [count], now_exclude_column, count + 1)
        bit_all_search(now_exclude_row, now_exclude_column, count + 1)
    elif H <= count:
        bit_all_search(now_exclude_row, now_exclude_column + [count - H], count + 1)
        bit_all_search(now_exclude_row, now_exclude_column, count + 1)


bit_all_search([], [], 0)

print(ans)

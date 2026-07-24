from bisect import bisect_left

N = int(input())
P = list(map(int, input().split()))


def prev_permutation(p):
    """
    1. 末尾から昇順になっている最長の部分列を探す⇒ p_last とする
    2. p_lastの長さがlen(p)ならNoneを返す
    3. 1つ前の要素を p_pre とする
    4. p_lastにp_preを追加する
    5. p_lastを昇順にソートする
    6. p_lastの中からp_preより小さい値の最大値(1.の条件より必ず存在する)を求め、p_lastから取り除く
    7. p_last を反転する
    8. [p_pre] + p_lastを pの残りと結合して返す
    """
    n = len(p)
    p_last_start = 0
    for i in range(n - 1)[::-1]:
        if p[i] >= p[i + 1]:
            p_last_start = i + 1
            break
    if p_last_start == 0:
        return None
    p_last = p[p_last_start - 1 :]
    p_pre = p[p_last_start - 1]
    p_last.sort()
    idx = bisect_left(p_last, p_pre)
    p_pre_new = p_last[idx - 1]
    p_last_rest = (p_last[: idx - 1] + p_last[idx:])[::-1]
    p_last = [p_pre_new] + p_last_rest
    return p[: p_last_start - 1] + p_last


Q = prev_permutation(P)
print(*Q)

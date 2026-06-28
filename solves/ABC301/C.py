S = input()
T = input()
alpha_num_S, alpha_num_T = S.count("@"), T.count("@")

ans = "Yes"
for c in "abcdefghijklmnopqrstuvwxyz":
    c_num_S, c_num_T = S.count(c), T.count(c)
    if c_num_S != c_num_T and c not in "atcoder":
        ans = "No"
    if c_num_S > c_num_T:
        alpha_num_T -= c_num_S - c_num_T
    else:
        alpha_num_S -= c_num_T - c_num_S

if alpha_num_S < 0 or alpha_num_T < 0:
    ans = "No"

print(ans)

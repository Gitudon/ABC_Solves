N = int(input())
S = list(map(str, input().split()))

ans = ""
for s in S:
    if "a" <= s[0] <= "c":
        ans += "2"
    elif "d" <= s[0] <= "f":
        ans += "3"
    elif "g" <= s[0] <= "i":
        ans += "4"
    elif "j" <= s[0] <= "l":
        ans += "5"
    elif "m" <= s[0] <= "o":
        ans += "6"
    elif "p" <= s[0] <= "s":
        ans += "7"
    elif "t" <= s[0] <= "v":
        ans += "8"
    elif "w" <= s[0] <= "z":
        ans += "9"

print(ans)

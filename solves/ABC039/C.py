S = input()

kenban = "WBWBWWBWBWBW" * 100
ans = ["Do", "Do", "Re", "Re", "Mi", "Fa", "Fa", "So", "So", "La", "La", "Si"]
for i in range(len(kenban) - len(S) + 1):
    if kenban[i : i + len(S)] == S:
        print(ans[i % 12])
        break

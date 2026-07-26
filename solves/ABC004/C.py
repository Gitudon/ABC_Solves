N = int(input())

N %= 30
cards = ["1", "2", "3", "4", "5", "6"]
for i in range(N):
    cards[(i % 5)], cards[(i % 5) + 1] = cards[(i % 5) + 1], cards[(i % 5)]

ans = ""
for c in cards:
    ans += c
print(ans)

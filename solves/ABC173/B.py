N = int(input())
dics = {}
for i in range(N):
    s = input()
    if s in dics:
        dics[s] += 1
    else:
        dics[s] = 1
print("AC x", dics.get("AC", 0))
print("WA x", dics.get("WA", 0))
print("TLE x", dics.get("TLE", 0))
print("RE x", dics.get("RE", 0))

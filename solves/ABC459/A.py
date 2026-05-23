X = int(input())

ans = ""
string = "HelloWorld"

for i in range(len(string)):
    if i != X - 1:
        ans += string[i]
print(ans)

N, T, A = map(int, input().split())
kahansu = N // 2
if T > kahansu or A > kahansu:
    print("Yes")
else:
    print("No")

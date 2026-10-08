X, Y = map(str, input().split())
vers = ["Ocelot", "Serval", "Lynx"]
if vers.index(X) >= vers.index(Y):
    print("Yes")
else:
    print("No")

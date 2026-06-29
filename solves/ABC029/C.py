N = int(input())


def abc(s):
    if len(s) == N:
        print(s)
        return
    abc(s + "a")
    abc(s + "b")
    abc(s + "c")


abc("")

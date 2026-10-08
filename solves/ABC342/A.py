S = input()


def main():
    for i in range(len(S) - 1):
        if S[i] != S[i + 1]:
            if i == 0:
                if S[i] != S[i + 2]:
                    print(1)
                else:
                    print(2)
            else:
                print(i + 2)
            return


main()

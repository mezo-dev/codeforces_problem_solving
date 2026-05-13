


def check_codeforces():
    target = "codeforces"

    t = int(input())
    for _ in range(t):
        a = input()

        if a in target:
            print("Yes")
        else:
            print("No")
    
check_codeforces()
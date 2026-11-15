


def bechgold_problem():
    n = int(input())

    k = n // 2
    print(k)

    if n % 2 == 0:
        print(*(2 for _ in range(k)))
    else:
        print(*(2 for _ in range(k -1)), 3)

bechgold_problem()
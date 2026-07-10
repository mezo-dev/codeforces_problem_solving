


def find_min():

    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())

        # equation = (c - a) + (b - c)
        print(b-a)



find_min()
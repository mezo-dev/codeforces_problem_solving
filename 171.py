


def restoring_3_nums():
    x = list(map(int, input().split()))
    x.sort()

    biggest = x[3]

    return [
        biggest - x[0],
        biggest - x[1],
        biggest - x[2]
    ]

print(*restoring_3_nums())
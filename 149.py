


def two_integer_problem():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())

        distance = abs(a - b)

        total_moves = (distance + 9) // 10

        print(total_moves) 


two_integer_problem()
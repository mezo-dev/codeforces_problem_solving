




def minutes_before_the_newyear():
    t = int(input())

    day_in_minuts = 1440

    for _ in range(t):
        h, m = map(int, input().split())


        result = (h * 60) + m - day_in_minuts
        print(abs(result))

minutes_before_the_newyear()
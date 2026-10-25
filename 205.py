




def minutes_before_the_newyear():
    t = int(input())

    whole_minutes_day = 1440
    for _ in range(t):
        h, m = map(int, input().split()) # 23 55 example of input format

        result = (h * 60) + m - whole_minutes_day
        print(abs(result))



minutes_before_the_newyear()
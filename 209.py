


def fair_playoff():
    t = int(input())

    for _ in range(t):
        s1, s2, s3, s4 = map(int, input().split())

        winner_1 = max(s1, s2)
        winner_2 = max(s3, s4)

        side_1_loser = min(s1, s2)
        side_2_loser = min(s3, s4)

        if side_1_loser > winner_2 or side_2_loser > winner_1:
            print("NO")
        else:
            print("Yes")

 

fair_playoff()




def long_legs_rebot():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())

        answer = a + b 
        m = 2

        while m - 1 < answer:
            jumps_x = (a + m - 1) // m
            jumps_y = (b + m - 1) // m

            moves = (m - 1) + jumps_x + jumps_y

            answer = min(answer, moves)
            m += 1
        
        print(answer)
    
long_legs_rebot()
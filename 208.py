


def math_problem(n: int) -> int:
    

    a, b = 0, 0

    while n % 2 == 0:
        n //= 2
        a += 1

    while n % 3 == 0:
        n //= 3
        b+= 1 

    if n != 1 or a > b:
        return -1
    
    return 2 * b -a


t = int(input())

for _ in range(t):
    n = int(input())
    print(math_problem(n))




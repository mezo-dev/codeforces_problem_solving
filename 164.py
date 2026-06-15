




def cut_ribbon():
    n, a, b, c = map(int, input().split())

    max_pieces = 0

    for x in range(n // a + 1):

        for y in range((n - a * x) // b + 1):
            remaining = n - (a * x + b * y)

        if remaining % c == 0:
            z = remaining //c 
            current_total = x + y + z
            if current_total  > max_pieces:
                max_pieces = current_total 
    print(max_pieces) 






cut_ribbon()
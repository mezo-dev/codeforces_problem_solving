



def guess_laptop():
    n = int(input())
    laptops = []

    for _ in range(n):
        a, b = map(int, input().split())
        laptops.append((a, b))


    print(laptops)

    laptops.sort()

    print(laptops)

    for i in range(1, n):
        if laptops[i][1] < laptops[i - 1][1]:
            print("Happy Alex")
            return
    print("Poor Alex")



guess_laptop()

def beautiful_arr():
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        arr.sort()

        if arr[0] == arr[-1]:
            print("NO")
        else:
            arr = [arr[-1]] + arr[:-1]

            print("YES")
            print(*arr)


beautiful_arr()

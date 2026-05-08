



def solve():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        n_arr = set(map(int, input().split()))

        if k in n_arr:
            print("Yes")
            break
        else: 
            print('No')

solve()
    
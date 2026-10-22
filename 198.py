



def coins():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        if n % 2 == 0:
            print("Yes")
        
        elif k % 2 != 0 and k <= n:
            print("YES") 

        else:
            print("No")

coins()
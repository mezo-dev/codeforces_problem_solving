



def katryoshka_maker():
    n, m, k = map(int, input().split())

    x = min(n, m, k)
    answer = x + min((n - x) // 2, k - x)

    print(answer)


katryoshka_maker()
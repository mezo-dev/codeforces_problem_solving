

def swap_first_character() -> str:
    t = int(input())

    for _ in range(t):
        a, b = map(str, input().split())

        a_first_char = a[0]
        b_first_char = b[0]
        print(f"{b_first_char}{a[1:]} {a_first_char}{b[1:]}")


swap_first_character()
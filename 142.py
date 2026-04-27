


def is_lucky(s: str) -> None:
    first_3 = sum(int(c) for c in s[:3])
    last_3 = sum(int(c) for c in s[3:])

    print("YES" if first_3 == last_3 else "NO")
    
t = int(input())
while t:
    s = input()
    is_lucky(s)
    t -= 1
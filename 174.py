


def card_game() -> int:
    n = int(input())
    cards = list(map(int, input().split()))

    left = 0
    right = n - 1

    Sereja = 0
    Dima = 0

    turn = 0 # 0 for sergja and 1 for dima

    while left <= right:
        if cards[left] > cards[right]:
            picked = cards[left]
            left += 1

        else:
            picked = cards[right]
            right -= 1
        
        if turn == 0:
            Sereja += picked
        else:
            Dima += picked

        turn = 1 - turn

    print(Sereja, Dima)
 


card_game()
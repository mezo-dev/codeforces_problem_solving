

def min_coins():
    coins = [1, 5, 10]
    amount = 18
    counter = 0

    coins.sort(reverse=True)

    for coin in coins:
        while amount >= coin:
            amount -= coin
            counter += 1

    print(counter)

        


min_coins()
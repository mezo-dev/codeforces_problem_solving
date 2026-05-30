


def max_num_of_coins():
    coins = [1, 5, 10, 20]
    amount = 47
    coins.sort(reverse=False)

    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
            
    print(count)

max_num_of_coins()
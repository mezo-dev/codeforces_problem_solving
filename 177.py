



def is_composite(num: int) -> bool:
    if num < 4:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
        
    return False



def learn_from_math():
    n = int(input())

    for x in range(4, n):
        y = n - x

        if is_composite(x) and is_composite(y):
            print(x, y)
            break

learn_from_math()
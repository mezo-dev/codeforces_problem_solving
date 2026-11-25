

def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)
    return fib_list

n = int(input())
print(*fibonacci(n))
    
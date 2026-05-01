




def find_middle_num(a: int, b: int, c: int) -> None:
    sum_of_all = (a + b + c)
    middle_number = sum_of_all - min(a, b, c) - max(a, b, c)

    print(middle_number)

t = int(input())

while t:
    a, b, c = map(int, input().split())
    find_middle_num(a,b,c)
    t -= 1
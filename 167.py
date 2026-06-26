



def odd_one_out():
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())

        if a == b:
            print(c)
        elif b == c:
           print(a)
        else:
            print(b)
        t =- 1
    
odd_one_out()



# t = int(input())
# a, b, c = map(int, input().split())

# repeted = sorted([a, b, c])[1]
# different = (a + b + c) - 2 * repeted
# print(different)



# t = int(input())

# for _ in range(t):
#     a, b, c = map(int, input().split())
#     print( a ^ b ^ c)
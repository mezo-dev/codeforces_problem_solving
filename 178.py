





def a_b():
    t = int(input())

    for _ in range(t):
        nums = input()

        a = nums[0]
        b = nums[-1]

        print(int(a) + int(b))

a_b()

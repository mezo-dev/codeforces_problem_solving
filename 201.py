






def collect_your_name():
    q = int(input())

    for _ in range(q):
        n = int(input())
        s, t = input().split()

        possible = True

        for char in s:
            if s.count(char) != t.count(char):
                possible = False
                break
        
        if possible:
            print('Yes')
        else:
            print('No')

collect_you_name()
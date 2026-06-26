from collections import Counter


def spy_detected():
    t = int(input())

    for _ in range(t):
        n_length = int(input()) 
        n_nums = list(map(int, input().split()))

        counter = Counter(n_nums)
        print(counter)
        for idx, num in enumerate(n_nums):
            if counter[num] == 1: # if the value of the counter idx num == 1 means this is the unique num (:
                print(idx+1)

spy_detected()




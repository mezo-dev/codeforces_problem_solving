





def good_kid():

    t = int(input())

    for _ in range(t):
        n = int(input())

        arr = list(map(int, input().split())) # example: 1 2 3 4 in each line

        arr.sort() # from smallest

        arr[0] += 1 # adding one to the smallest num in the arr


        product = 1
        for x in arr:
            product *= x # to can mulitple each number with next one to get the max
        
        print(product)

good_kid()
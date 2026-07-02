



def police_officers():

    n = int(input())
    n_crimes = list(map(int, input().split()))

    free_police_officers = 0
    untreated_crimes = 0

    for i in n_crimes:
        if i == -1:

            if free_police_officers:
                free_police_officers -= 1
            else:
                untreated_crimes += 1
        else:
            free_police_officers += i

    return untreated_crimes


print(police_officers())


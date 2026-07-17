



def short_sort():

    t = int(input())

    target = "abc"

    for _ in range(t):
        word = input()

        if word == target:
            print("Yes")
            continue 
        
        chars = list(word)
        found = False

        chars[0], chars[1] = chars[1], chars[0] 
        if "".join(chars) == target:
            found = True
        chars[0], chars[1] = chars[1], chars[0]

        if not found:
            chars[0], chars[2] = chars[2], chars[0]
            if "".join(chars) == target:
                found = True
            chars[0], chars[2] = chars[2], chars[0]

        if not found:
            chars[1], chars[2] = chars[2], chars[1]
            if "".join(chars) == target:
                found = True
            chars[1], chars[2] = chars[2], chars[1]

        print("Yes" if found else "No")


short_sort()
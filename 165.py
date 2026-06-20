




def vanya_and_fence():
    n, h = map(int, input().split())
    heights = list(map(int, input().split()))

    total_width = 0

    for height in heights:
        if height > h:
            total_width += 2
        else:
            total_width += 1

    return total_width


print(vanya_and_fence())




def task_distracted():

    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().upper()

        seen = set()
        previous = ""
        valid = True

        for letter in s:
            if letter == previous:
                continue

            if letter in seen:
                valid = False
                break

            seen.add(letter)
            previous = letter
        
        print("YES" if valid else "No")


task_distracted()

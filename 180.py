


def love_story() -> int:
    target_word = "codeforces"
    t = int(input())

    for _ in range(t):
        s = input()
        count = 0

        for idx, ch in enumerate(s):
            if ch != target_word[idx]:
                count += 1
                
        print(count)

love_story()
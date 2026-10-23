


def spell_check():
    t = int(input())
    answers = []

    for _ in range(t):
        n = int(input())
        s = input()
        
        if sorted(s) == sorted("Timur"):
                answers.append("Yes")
        else:
            answers.append("No")

    return answers

print(*spell_check(), sep="\n")
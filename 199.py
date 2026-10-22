
def chat_order():
    n = int(input())
    messages = [input() for _ in range(n)]

    chats = []
    seen = set()

    for recipient in reversed(messages):
        if recipient not in seen:
            chats.append(recipient)
            seen.add(recipient)

    return chats


print(*chat_order(), sep="\n")

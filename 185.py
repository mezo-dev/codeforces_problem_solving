




def find_word_in_sentance(sentance: str, word: str):
    for j in range(len(sentance)):
        if sentance[j:j + len(word)] == word:
            return f"Word is found and start at index {j}"
    return False


print(find_word_in_sentance("i love python so much", "so"))





numbers = [3, 3, 2, 3]


def count_duplicated(numbers: list[int]) -> dict:
    counter = dict()

    for num in numbers:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1

    print(counter)


count_duplicated(numbers)
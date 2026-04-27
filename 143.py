


def puzzle(n: int, m: int, puzzles: list[int]):
    puzzles.sort()
    min_diff = float("inf")

    for i in range(m - n + 1):
        current = puzzles[i : i + n]
        diff = current[-1] - current[0]

        min_diff = min(min_diff, diff)
    print(min_diff)
 
n, m = map(int, input().split())
puzzles = list(map(int, input().split()))

puzzle(n, m, puzzles)
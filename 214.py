


def convert_to_binary(num: int):
    if num == 0:
        return "0"
    
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num //= 2
    return binary

def convert_to_decimal(binary: str) -> int:
    decimal = 0
    for idx, dight in enumerate(reversed(binary)):
        if dight == "1":
            decimal += 2 ** idx

    return decimal

def main(n: int) -> int:

    c = convert_to_binary(n).count("1")
    return convert_to_decimal("1" * c)


t = int(input())
for i in range(t):
    n = int(input())
    print(main(n))
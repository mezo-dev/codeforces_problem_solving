from decimal import Decimal

            
class ConvertBinary:
    def __init__(self) -> None:
        ...

    @staticmethod
    def to_decimal(binary_number: str) -> Decimal:
        total = 0
        powered = 1

        for y in reversed(binary_number):
            if y == '1':
                total += powered
            powered *= 2
        return total

    @staticmethod
    def to_binary(number: Decimal) -> str:
        if number == 0:
            return "0"
        
        bits = []
        while number > 0:
            bits.append((str(number & 1)))
            number >>= 1
        return "".join(reversed(bits))
        



print(ConvertBinary.to_decimal(binary_number="1011001"))
print(ConvertBinary.to_binary(number=89))
        



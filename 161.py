
power = 2

x =int(input())
answer = 0

while x > 0:
    largest = 1 << (x.bit_length() - 1)
    x = x - largest
    answer += 1

print(answer)


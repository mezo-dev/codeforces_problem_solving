



x = int(input())

counter = 0

for y in bin(x):
    if y == "1":
        counter+=1
print(counter)
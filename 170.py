



def decoded_ternary():
    borze_code = input()

    number = []

    i = 0
    while i < len(borze_code):
        if borze_code[i] == ".":
            number.append(0)
            i += 1
        elif borze_code[i + 1] == ".":   
            number.append(1)
            i += 2
        else:                            
            number.append(2)
            i += 2

    return number

print(*decoded_ternary(), sep="")
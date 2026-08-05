




def swap_and_delete():

    for _ in range(int(input())):
        s = input()

        zeros = s.count("0")
        ones = s.count("1")

        matched = 0

        for i in s:

            if i == "0":
                if ones == 0:
                    break
                ones -= 1

            else:
                if zeros ==  0:
                    break
                zeros -= 1

            matched += 1
        print(len(s) - matched)


swap_and_delete()
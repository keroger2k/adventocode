numbers = open("day-one-input.txt", "r").readlines()

for n in numbers:
    for nn in numbers:
        for nnn in numbers:
            result = int(n) + int(nn) + int(nnn)
            if result == 2020:
                print("Total sum for %s and %s and %s is 2020" % (int(n) , int(nn), int(nnn)))
                print("Product is %s" % (int(n)*int(nn)*int(nnn)))


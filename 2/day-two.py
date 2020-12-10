passwords = open("2\day-two-input.txt", "r").readlines()
count = 0

for p in passwords:
    policy = p.split( )
    min = int(policy[0].split("-")[0])
    max = int(policy[0].split("-")[1])
    letter = policy[1].split(":")[0]
    pass1 = policy[2]
    #print("Min: %s, Max: %s, Letter: %s, Pass: %s" % (min,max,letter,pass1))
    #occurences = pass1.count(letter)
    #if occurences >= min and occurences <= max:
    #    count = count + 1
    #    print(occurences)
    #    print(policy)

    position1 = pass1[min-1]
    position2 = pass1[max-1]

    if position1 == letter and position2 != letter:
        count = count + 1
    elif position1 != letter and position2 == letter:
        count = count + 1
    

    #print(position1)
    #print(position2)

print(count)

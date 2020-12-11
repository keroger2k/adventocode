input = open("3\day-three-input.txt", "r").readlines()

row_width = len(input[0]) - 1
column_height = len(input) - 1

x_spaces = 1
y_spaces = 1

right = 1
down = 1

trees = 0

for i in range(0,column_height,y_spaces):
    if down > column_height:
        break

    if right >= row_width:
        right = right - row_width
    result = input[down][right]
    
    if result == '#':
        trees = trees + 1

    print("Found a %s @ [%s,%s]" % (result, down, right))

    right = right + x_spaces
    down = down + y_spaces

print(trees)
    
# write your code here
"""print('''X O X
O X O
X X O''')"""
"""item_input = input()
print('-' * 9)
print(f'| {" ".join(item_input[0:3])} |')
print(f'| {" ".join(item_input[3:6])} |')
print(f'| {" ".join(item_input[6:9])} |')
print('-' * 9)"""


"""def print_matrix(m):
    print('-' * 9)
    for line in m:
        print(f'| {line[0]} {line[1]} {line[2]} |')
    print('-' * 9)


item_input = input()
matrix = []
x, y = [0, 3]
for i in range(3):
    lst = [i for i in item_input[x:y]]
    x += 3
    y += 3
    matrix.append(lst)
print_matrix(matrix)
if item_input.count('X') - item_input.count('O') > 1\
        or item_input.count('O') - item_input.count('X') > 1\
        or item_input.count('X') == 4 and item_input.count('O') == 3:
    print('Impossible')
else:
    if matrix[0][0] == "X":
        if matrix[0][1] == "X" and matrix[0][2] == "X":
            print('X wins')
        elif matrix[1][0] == "X" and matrix[2][0] == "X":
            print('X wins')
        elif matrix[1][1] == "X" and matrix[2][2] == "X":
            print('X wins')
        elif item_input.count('X') + item_input.count('O') != 9 \
                and item_input.count('_') > 0 or item_input.count(' ') > 0:
            print("Game not finished")
        else:
            print('Draw')
    if matrix[0][0] == "O":
        if matrix[0][1] == "O" and matrix[0][2] == "O":
            print('O wins')
        elif matrix[1][0] == "O" and matrix[2][0] == "O":
            print('O wins')
        elif matrix[1][1] == "O" and matrix[2][2] == "O":
            print('O wins')
        elif item_input.count('X') + item_input.count('O') != 9 \
                and item_input.count('_') > 0 or item_input.count(' ') > 0:
            print("Game not finished")
        else:
            print('Draw')
    if matrix[0][2] == "X":
        if matrix[0][1] == "X" and matrix[0][0] == "X":
            print('X wins')
        elif matrix[1][2] == "X" and matrix[2][2] == "X":
            print('X wins')
        elif matrix[1][1] == "X" and matrix[2][0] == "X":
            print('X wins')
        elif item_input.count('X') + item_input.count('O') != 9 \
                and item_input.count('_') > 0 or item_input.count(' ') > 0:
            print("Game not finished")
        else:
            print('Draw')
    if matrix[0][2] == "O":
        if matrix[0][0] == "O" and matrix[0][2] == "O":
            print('O wins')
        elif matrix[1][2] == "O" and matrix[2][2] == "O":
            print('O wins')
        elif matrix[1][1] == "O" and matrix[2][0] == "O":
            print('O wins')
        elif item_input.count('X') + item_input.count('O') != 9 \
                and item_input.count('_') > 0 or item_input.count(' ') > 0:
            print("Game not finished")
        else:
            print('Draw')
    if matrix[0][1] == 'X':
        if matrix[1][1] == 'X' and matrix[2][2] == "X":
            print('X wins')
    if matrix[0][1] == 'O':
        if matrix[1][1] == 'O' and matrix[2][1] == "O":
            print('O wins')
"""


def print_matrix(item):
    matrix = []
    x, y = [0, 3]
    for i in range(3):
        lst = [i for i in item[x:y]]
        x += 3
        y += 3
        matrix.append(lst)
    print('-' * 9)
    for line in matrix:
        print(f'| {line[0]} {line[1]} {line[2]} |')
    print('-' * 9)
    global stop
    if matrix[0][0] == "X":
        if matrix[0][1] == "X" and matrix[0][2] == "X":
            print('X wins')
            stop = False
        elif matrix[1][0] == "X" and matrix[2][0] == "X":
            print('X wins')
            stop = False
        elif matrix[1][1] == "X" and matrix[2][2] == "X":
            print('X wins')
            stop = False
    if matrix[0][0] == "O":
        if matrix[0][1] == "O" and matrix[0][2] == "O":
            print('O wins')
            stop = False
        elif matrix[1][0] == "O" and matrix[2][0] == "O":
            print('O wins')
            stop = False
        elif matrix[1][1] == "O" and matrix[2][2] == "O":
            print('O wins')
            stop = False
    if matrix[0][2] == "X":
        if matrix[0][1] == "X" and matrix[0][0] == "X":
            print('X wins')
            stop = False
        elif matrix[1][2] == "X" and matrix[2][2] == "X":
            print('X wins')
            stop = False
        elif matrix[1][1] == "X" and matrix[2][0] == "X":
            print('X wins')
            stop = False
    if matrix[0][2] == "O":
        if matrix[0][0] == "O" and matrix[0][2] == "O":
            print('O wins')
            stop = False
        elif matrix[1][2] == "O" and matrix[2][2] == "O":
            print('O wins')
            stop = False
        elif matrix[1][1] == "O" and matrix[2][0] == "O":
            print('O wins')
            stop = False
    if matrix[0][1] == 'X':
        if matrix[1][1] == 'X' and matrix[2][2] == "X":
            print('X wins')
            stop = False
    if matrix[0][1] == 'O':
        if matrix[1][1] == 'O' and matrix[2][1] == "O":
            print('O wins')
            stop = False


def x_step(item):
    while True:
        global item_input, count
        coordinate = input('Enter the coordinates: > ').split()
        if coordinate[0].isalpha() or coordinate[1].isalpha():
            print('You should enter numbers!')
        elif int(coordinate[0]) > 3 or int(coordinate[1]) > 3:
            print('Coordinates should be from 1 to 3!')
        else:
            if int(coordinate[1]) == 1:
                place = 5 + int(coordinate[0])
                item = list(item)
                if item[place] == '_':
                    item[place] = 'X'
                    item = ''.join(item)
                    print_matrix(item)
                    item_input = item
                    count += 1
                    break
                else:
                    print("This cell is occupied! Choose another one!")

            elif int(coordinate[1]) == 2:
                place = 2 + int(coordinate[0])
                item = list(item)
                if item[place] == '_':
                    item[place] = 'X'
                    item = ''.join(item)
                    print_matrix(item)
                    item_input = item
                    count += 1
                    break
                else:
                    print("This cell is occupied! Choose another one!")

            elif int(coordinate[1]) == 3:
                place = -1 + int(coordinate[0])
                item = list(item)
                if item[place] == '_':
                    item[place] = 'X'
                    item = ''.join(item)
                    print_matrix(item)
                    item_input = item
                    count += 1
                    break
                else:
                    print("This cell is occupied! Choose another one!")


def o_step(item):
    while True:
        global item_input, count
        coordinate = input('Enter the coordinates: > ').split()
        if coordinate[0].isalpha() or coordinate[1].isalpha():
            print('You should enter numbers!')
        elif int(coordinate[0]) > 3 or int(coordinate[1]) > 3:
            print('Coordinates should be from 1 to 3!')
        else:
            if int(coordinate[1]) == 1:
                place = 5 + int(coordinate[0])
                item = list(item)
                if item[place] == '_':
                    item[place] = 'O'
                    item = ''.join(item)
                    print_matrix(item)
                    item_input = item
                    count += 1
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            elif int(coordinate[1]) == 2:
                place = 2 + int(coordinate[0])
                item = list(item)
                if item[place] == '_':
                    item[place] = 'O'
                    item = ''.join(item)
                    print_matrix(item)
                    item_input = item
                    count += 1
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            elif int(coordinate[1]) == 3:
                place = -1 + int(coordinate[0])
                item = list(item)
                if item[place] == '_':
                    item[place] = 'O'
                    item = ''.join(item)
                    print_matrix(item)
                    item_input = item
                    count += 1
                    break
                else:
                    print("This cell is occupied! Choose another one!")


#item_input = input('Enter cells: > ')
item_input = '_________'
print_matrix(item_input)
count = 1
stop = True
while count != 10:
    if not stop:
        break
    elif count % 2 != 0:
        x_step(item_input)
    else:
        o_step(item_input)
else:
    if stop:
        print("Draw")

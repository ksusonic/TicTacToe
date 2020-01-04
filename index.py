def output():
    print('-' * 9)
    for i in range(0, len(cells), 3):
        row = cells[i:i + 3]
        for i in range(len(row)):
            if row[i] == '_':
                row[i] = " "
        print(f'| {" ".join(row)} |')
    print('-' * 9)

def check():
    win_X = False
    win_O = False
    n_finished = False

    # vertical
    for i in range(3):
        if cells[i] == cells[i+3] == cells[i+6]:
            if cells[i] == 'X':
                win_X = True
            elif cells[i] == 'O':
                win_O = True

    # horizontal
    for i in range(0,7,3):
        if cells[i] == cells[i+1] == cells[i+2]:
            if cells[i] == 'X':
                win_X = True
            elif cells[i] == 'O':
                win_O = True
                
    # diagonal
    if cells[0] == cells[4] == cells[8]:
         if cells[0] == 'X':
                win_X = True
         elif cells[0] == 'O':
                win_O = True

    if cells[2] == cells[4] == cells[6]:
        if cells[2] == 'X':
                win_X = True
        elif cells[2] == 'O':
                win_O = True

    # not finished check:
    if '_' in cells:
        n_finished = True

    # count:
    x_count = 0
    o_count = 0
    for i in cells:
        if i == 'X':
            x_count += 1
        elif i == 'O':
            o_count += 1


    if win_O and win_X or x_count - o_count >= 2 or o_count - x_count >= 2:
        return 'Impossible'
    elif n_finished and not win_O and not win_X:
        return 'Game not finished'
    elif not win_X and not win_O:
        return 'Draw'
    elif win_X:
        return 'X wins'
    elif win_O:
        return 'O wins'

def place(sign):
    try:
        x, y = [int(x) for x in input('Enter the coordinates: ').split()]
    except ValueError:
        print('You should enter numbers!')
        place(sign)
        return 0

    if x > 3 or x < 1 or y > 3 or y < 1:
        print("Coordinates should be from 1 to 3!")
        place(sign)
        return 0

    y = 3 - y
    z = (x - 1) + (3 * y)

    if cells[z] == '_':
        cells[z] = sign
    else:
        print('This cell is occupied! Choose another one!')
        place(sign)

# main
cells = ['_' for i in range(9)]
output()
for i in range(9):
    if i % 2 == 1:
        place('X')
    else:
        place('O')
    output()
    if check() != 'Game not finished':
        print(check())
        break

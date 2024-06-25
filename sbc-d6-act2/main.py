def box(width, height):
    row = 0
    while row < height:
        col = 0
        while col < width:
            if row == 0 or row == height - 1 or col == 0 or col == width - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
            col += 1
        print()
        row += 1

row = int(input("Enter row: "))
column = int(input("Enter Column: "))
box(row, column)

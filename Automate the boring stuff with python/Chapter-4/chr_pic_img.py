grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

row_size = 0
for max_ln in grid:
    if row_size < len(max_ln):
        row_size = len(max_ln) # i added this line cause i though if the inner list has different length

for column in range(row_size):
    for row in range(len(grid)):
        print(grid[row][column], end=' ')
    print()

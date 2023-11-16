def printtbale(tableData):
    colWidths = [0] * len(tableData)
    for list_ in range(len(tableData)):
        colWidths[list_] = max(len(word) for word in tableData[list_])

    for list_ in range(len(tableData[1])):
        for element in range(len(tableData)):
            print(tableData[element][list_].rjust(colWidths[element]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']
             # ,['laptop', 'desktop', 'supercomputer', 'server']
             ]
# print(len(tableData))


printtbale(tableData)

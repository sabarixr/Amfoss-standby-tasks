def displayInventory(items_in):
    print('Inventory: \n')
    total = 0
    for item,no in items_in.items():
        print(f'{no} {item}')
        total += no
    print(f'Total number of items: {total}')


things = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(things)

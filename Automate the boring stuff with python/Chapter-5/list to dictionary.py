def displayInventory(items_in):
    print('Inventory: \n')
    total = 0
    for item, no in items_in.items():
        print(f'{no} {item}')
        total += no
    print(f'Total number of items: {total}')

def addToInventory(inventory, addedItems):
    print(addedItems)
    for itm in addedItems:
        if itm not in inventory:
            inventory.setdefault(itm, 1)
        else:
            inventory[itm] += 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

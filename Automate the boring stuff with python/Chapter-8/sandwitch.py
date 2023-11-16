import pyinputplus as pyin
from pprint import pprint

price = {
    'wheat': 5,
    'white': 3,
    'sourdough': 6,
    'chicken': 5,
    'turkey': 6,
    'ham': 4,
    'tofu': 2,
    'cheddar': 1,
    'Swiss': 2,
    'mozzarella': 1,
    'mayo': 0.5,
    'mustard': 0.5,
    'lettuce': 1,
    'tomato ': 1
}

def grand_total(orders):
    total_cost = 0
    for item in orders.keys():
        total_cost += price[orders[item]]
    return total_cost

order = {}
while True:
    order['bread'] = pyin.inputMenu(prompt='Enter the type of bread you want\n',
                                    choices=['wheat', 'white', 'sourdough'])
    order['protein'] = pyin.inputMenu(prompt='Enter the type of protein you want to add\n',
                                      choices=['chicken', 'turkey', 'ham', 'tofu'])
    y_cheese = pyin.inputYesNo(prompt='Do you want cheese? (yes/no): ')
    if y_cheese == 'yes':
        order['cheese'] = pyin.inputMenu(prompt='Choose the type of cheese you want \n',
                                         choices=['cheddar', 'Swiss', 'mozzarella'])
    y_dips = pyin.inputYesNo(prompt='Do you want to add extra dips to the order? (yes/no): ')
    if y_dips == 'yes':
        order['dips'] = pyin.inputMenu(prompt='Choose a dip', choices=['mayo', 'mustard', 'lettuce', 'tomato'])
    order_num = pyin.inputInt(prompt='Enter the number of orders: ')

    pprint(order)

    order_conf = pyin.inputYesNo(prompt='Type yes to confirm the order : ')

    if order_conf == 'yes':
        break


total_sub = grand_total(order)
total = total_sub * order_num
print(f'\n\nYour grand total is {total}')




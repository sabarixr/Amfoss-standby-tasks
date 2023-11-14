def collatz(number):
    if number % 2 == 0 :
        value = number // 2
        print(value)
        return value
    else:
        value = 3 * number + 1
        print(value)
        return value

number = int(input('enter the number which you want to find the sequence of: '))
while number != 1 :
    number = collatz(number)
import re

def valid_date(date_):
    dateregx = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
    date_match = dateregx.search(date_)

    if not date_match:
        print('Entered date is not correct')
        return False

    day = int(date_match.group(1))
    month = int(date_match.group(2))
    year = int(date_match.group(3))


    month_30 = ['04', '06', '09', '11']
    month_31 = ['01', '03', '05', '07', '08', '10', '12']

    if not (1 <= day <= 31):
        print("Invalid day entered")
        return False

    if not (1 <= month <= 12):
        print('Invalid month')
        return False

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                print("Invalid day for february in a leap year")
                return False
        elif day > 28:
            print("Invalid day in february")
            return False
    month = str(month)
    if (month in month_30 and day > 30) or (month in month_31 and day > 31):
        print("Invalid day for this month")
        return False

    print(f"{date_} is a valid date")
    return True

while True:
    inp = input('Enter the date in DD/MM/YYYY( ' ' to stop the loop): ')

    if inp == ' ':
        break

    torf = valid_date(inp)

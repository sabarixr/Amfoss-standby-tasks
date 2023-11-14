import re


def valid_password(password):
    if len(password) < 8:
        return False

    if not (re.search(r'\d', password)):
        return False

    if not (re.search(r'[A-Z]', password)):
        return False
    if not (re.search(r'[a-z]', password)):
        return False

    return True


while True:
    pas = input("Enter the password(' ' to stop teh loop): ")

    if pas == ' ':
        break
    else:
        torf = valid_password(pas)

    if torf:
        print(f'{ pas } is indeed a strong password')
    else:
        print(f'{ pas } is more of a weak password')

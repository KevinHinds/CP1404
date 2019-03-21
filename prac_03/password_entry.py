"""Kevin Hinds"""

MINIMUM_LENGTH = 6


def main():
    password = get_password(MINIMUM_LENGTH)
    print_astericks(password)


def get_password(minimum_length):
    password = input("Please enter password of at least {} length: ".format(MINIMUM_LENGTH))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Please enter password of at least {} length: ".format(MINIMUM_LENGTH))
    return password


def print_astericks(length_of_password):
        print('*' * len(length_of_password))


main()


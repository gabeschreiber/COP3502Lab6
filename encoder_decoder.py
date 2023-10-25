# Gabriel Schreiber

def encode(password):
    raw_password = list(password)
    encoded_password = []
    run = True
    while run:
        try:
            for num in raw_password:
                encoded_password.append(int(num) + 3)
            run = False
        except ValueError:
                encoded_password.clear()
                raw_password = list(input('Please enter valid password: '))
    print('Your password has been encoded and stored!\n')
    return encoded_password


def main():
    print('Menu\n' + ('-' * 13) + '\n1. Encode\n2. Decode\n3. Quit\n')
    user_input = int(input('Please enter an option: '))
    while user_input != 3:
        if user_input == 1:
            encoded_password = encode(input('Please enter your password to encode: '))
        elif user_input == 2:
            # FIXME add call to decode function
            print()
        print('Menu\n' + ('-' * 13) + '\n1. Encode\n2. Decode\n3. Quit\n')
        user_input = int(input('Please enter an option: '))


if __name__ == '__main__':
    main()

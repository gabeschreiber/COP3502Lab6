# Gabriel Schreiber

def encode(password):
    raw_password = list(password)
    encoded_password = ''
    run = True
    while run:
        try:
            for num in raw_password:
                new_num = int(num) + 3
                if new_num > 9:
                    encoded_password += str(new_num - 10)
                else:
                    encoded_password += str(new_num)
            run = False
        except ValueError:
                encoded_password.clear()
                raw_password = list(input('Please enter valid password: '))
    print('Your password has been encoded and stored!\n')
    return encoded_password

# Andrea Louis
def decode(encoded_password):
    raw_password = list(encoded_password)
    decoded_password = ''
    # the for loop iterates through the numbers and converts it back to the original string entered by the user
    for num in raw_password:
        # the string is changed to an integer and then subtracted by three to be stored in the variable
        new_num = int(num) - 3
        if new_num < 0:
            # 10 is added to make sure it is the valid digit converted within the range
            decoded_password += str(new_num + 10)
        else:
            # the new_num variable is changed to a string
            decoded_password += str(new_num)
    return decoded_password

def main():
    print('Menu\n' + ('-' * 13) + '\n1. Encode\n2. Decode\n3. Quit\n')
    user_input = int(input('Please enter an option: '))
    while user_input != 3:
        if user_input == 1:
            encoded_password = encode(input('Please enter your password to encode: '))
        elif user_input == 2:
            print(f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.')
            print()
        print('Menu\n' + ('-' * 13) + '\n1. Encode\n2. Decode\n3. Quit\n')
        user_input = int(input('Please enter an option: '))


if __name__ == '__main__':
    main()

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
    print('Your password has been encoded and stored!')
    return encoded_password


def main():
    encoded_password = encode(input('Please enter your password to encode: '))


if __name__ == '__main__':
    main()

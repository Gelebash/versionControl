#Aaron Song
#(partner name)

#Prints menu
def printMenu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

#Gets user input
def userInput():
    opt = input('Please enter an option: ')
    return int(opt)

#Encodes password 
def encode() -> int:
    password = input('Please enter your password to encode: ')
    new_password = ''
    for i in password:
        temp = int(i)
        new_password += str((temp+4)%10)
    return new_password

def main():
    loop = True
    while loop:
        printMenu()
        option = userInput()

        match option:
            case 1:
                password = encode()
                return('Your password has been encoded and stored!\n')
            case 2:
                pass
            case 3:
                option = False

if __name__ == '__main__':
    main()
#Aaron Song
#(Garrett Elebash)

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
        new_password += str((temp+3)%10)
    return new_password

def decode(password):
    new_password = ''
    for i in password:
        temp = int(i)
        if temp < 3:
            temp = 10 + temp-3
        else:
            temp-=3
        new_password += str(temp)
    return new_password

def main():
    loop = True
    while loop:
        printMenu()
        option = userInput()
        print
        match option:
            case 1:
                password = encode()
                print('Your password has been encoded and stored!\n')
            case 2:
                decoded = decode(password)
                print(f'Your encoded password is {password}, and your original password is {decoded}\n')
            case 3:
                loop = False

if __name__ == '__main__':
    main()
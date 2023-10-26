#aicha keita encoder 
def menu():
    print("Menu")
    print('-------------')
    print("1. Encode")
    print('2. Decode')
    print('3. Quit')
    print(' ')

def encode(password):
    new_pass = ""
    for i in range(len(password)):
        #shift ever number three digits 
        if int(password[i]) < 7: 
            new_pass += str(int(password[i]) + 3)
        #loop the numbers if they become 2 digits after adding three
        else:
            temp = str(int(password[i]) + 3)
            new_pass += temp[-1]
    
    return new_pass

#def decode(password):
    #og_pass = ""
    #for i in range(len(password)):
        #if int(password[i]) > 2:
            #og_pass += str(int(password[i]) - 3)
        #elif int(password[i]) =< 2:
            #temp = int(password[i]) + 10
            #og_pass += str(int(temp) - 3)
    
    #return og_pass

if __name__ == '__main__':
    menu()

    print("Please enter an option:")
    option = int(input())

    while option != 3:
        if option == 1:
            print("Please enter your password to encode:")
            password = str(input())
            new_pass = encode(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            #password = decode(new_pass)
            print("The encoded password is " + new_pass + ", and the original password is " + password)
        
        elif option == 3: 
            continue

        print('')
        menu()

        print("Please enter an option:")
        option = int(input())

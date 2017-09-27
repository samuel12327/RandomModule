from random import randint
def YourPINis ():
    print("Your PIN is:")
def main ():
    while True:
        length = int(input("Enter Length of PIN: "))
        YourPINis()
        for pin in range(0, length):
            print(randint(0, 9), end='')
        print("")
main()

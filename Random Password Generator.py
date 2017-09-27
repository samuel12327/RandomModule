import random
var = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","-", "=", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
     "_", "+", "`", "~", "[", "]", ";", "'", ",", ".", "/", "{", "}", "|", ":", '"', "<", ">", "?", "q", "w", "e", "r"
     , "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"
     , "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V"
     , "V", "B", "N", "M"]
def YourPass ():
    print("Your Password is:")
def main():
    while True:
        length = int(input("Enter Length of Password: "))
        YourPass()
        for password in range(0, length):
            print(random.choice(var), end="")
        print("")
main()

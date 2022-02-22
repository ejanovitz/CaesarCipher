# Caesar Cipher
# by Ethan Janovitz
# April 17, 2020 (High School - Grade 10)


def menu(title, items):
    """ Displays Menu """
    print(title.center(60, "-"))
    # Displays menu options
    for item in items:
        print(item)

    return int(input("\nEnter your selection: "))


def encrypt():
    """ Encrypts message using provided rotation """
    message = input("Enter a message: ")
    rotation = int(input("Enter a rotation number: "))
    new_message = translate(message, rotation)
    print("".join(new_message))


def decrypt():
    message = input("Enter a message: ")
    rotation = int(input("Enter a rotation number or 0 if unknown: "))
    if rotation == 0:
        # Runs the decryption 26 times to get all the possibilities
        print("Possible Decryptions:\n")
        for rotation in range(1, 26):
            new_message = translate(message, rotation)
            print(str(rotation) + ". " + "".join(new_message))
    else:
        # Multiply the rotation by -1 so make in shift backwards
        rotation = rotation * -1
        new_message = translate(message, rotation)
        print("".join(new_message))

# Checks to ensure letter is in alphabet. Adjusts the ordinate depending
# on whether the letter is upper or lower case. Divides the result of the
# letter ordinate, adjustment and rotation by 26 and uses the remainder
# in order loop the alphabet no matter how large the rotation number is


def translate(message, rotation):
    new_message = []
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                adjustment = 65
            else:
                adjustment = 97
            letter = (ord(letter) - adjustment + rotation) % 26
            letter = chr(letter + adjustment)
        new_message.append(letter)
    return new_message


endProgram = False

while not endProgram:
    # what the menu is going to print
    menuItems = ["1. Encrypt message", "2. Decrypt message", "3. End program"]

    selection = menu("Caesar Cipher", menuItems)
    # Calls the function depending on what the user selects
    if selection == 1:
        encrypt()
    elif selection == 2:
        decrypt()
    else:
        endProgram = True

import string as st
import random as rd

def printPassword(password):
    # Print the recommended password
    print(f"Kartik's Recommended password is: {password}.")
    return None

def chooseLength(choice):
    if choice == "yes":
        # If the user chooses to specify the password length
        num = int(input("Enter the number of digits you want: "))
        letters = int(input("Enter the number of letters you want: "))
        spChar = int(input("Enter the number of special characters you want: "))
        generatePassword(num, letters, spChar)

    else:
        # If we choose to use a default password length
        length = 17
        num = rd.randint(1, length - 4)  # Ensuring at least one digit
        length -= num
        letters = rd.randint(1, length - 3)  # Ensuring at least one letter
        spChar = length - letters  # All remaining characters are special characters
        generatePassword(num, letters, spChar)

def generatePassword(num, letters, spChar):
    password = ''
    length = num + letters + spChar

    while True:
        if length == 0:
            break

        else:
            randomChoice = rd.choice(["Num", "Letters", "SpChars"])

            if randomChoice == "Num" and num > 0:
                password += str(rd.choice(st.digits))
                num -= 1
                length -= 1

            elif randomChoice == "Letters" and letters > 0:
                password += str(rd.choice(st.ascii_letters))
                letters -= 1
                length -= 1

            elif randomChoice == "SpChars" and spChar > 0:
                password += str(rd.choice(st.punctuation))
                spChar -= 1
                length -= 1

    printPassword(password)


def main():
    print("\nWelcome to Kartik's Password Generator!")

    while True:
        # Get user input for choosing the password length
        response = input("\nDo you wish to define password length (yes or no): ").lower()

        # Call the function based on user's choice
        chooseLength(response)

        choice = input("Do you want another password to be generated? (yes or no): ")
        if choice.lower() == "yes":
            continue
        else:
            print("\nThank you for using Kartik's Password Generator!\nHope it helps :) ")
            break

if __name__ == "__main__":
    main()
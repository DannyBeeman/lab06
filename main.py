def password_encoder(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password
password = str(input())
encoded_password = password_encoder(password)
print(encoded_password)
#comment

def password_decoder(password): # Meynard Guillermo
    temp_password = int(password)
    for i in password:
        temp_password[i] -= 3
    return temp_password

def main():
    option = True
    while option:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")

        option = input("Please enter an option: ")

        if option == "1":
            password_encoder(password)
        elif option == "2":
            password_decoder(password)
        elif option == "3":
            option = False


if __name__ == "__main__":
    main()
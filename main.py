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
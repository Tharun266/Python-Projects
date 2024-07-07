import random

def generate_password(length):
    # Characters to use for generating the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    
    # Initialize the password variable
    password = ""
    
    # Generate the password
    for i in range(length):
        password += random.choice(characters)
    
    return password

while True:
    try:
        length = int(input("Enter the desired length for the password (minimum 1): "))
        if length < 1:
            print("Please enter a length of at least 1.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

password = generate_password(length)
print(f"Generated password: {password}")

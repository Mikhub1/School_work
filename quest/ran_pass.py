# Generate and display a random password containing between
# SHORTEST and LONGEST characters.
from random import randint
SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33 # define range of characters to
MAX_ASCII = 126 # randomly select from

# Generate a random password
def randomPassword():
# select a random length
    ran_len = randint(SHORTEST,LONGEST)
    password = ""
    for i in range(ran_len):
        ran_char = chr(randint(MIN_ASCII,MAX_ASCII))
        password += ran_char
    return password
    
# Check whether a password is good
# "Good" requires:
# - at least 8 characters long
# - contains at least one uppercase letter
# - contains at least one lowercase letter
# - contains at least one number
# Return True if the password is good, or False otherwise

def checkPassword(password):
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in password:
        if ch>= "A" and ch <= "Z":
            has_upper = True
        if ch>="a" and ch <="z":
            has_lower = True
        if ch>= "0" and ch <= "9":
            has_digit = True
        if len(password) >= 8 and has_upper and has_lower and has_digit:
            return True
    return False

def main():
    p = input("Enter a password: ")
    if checkPassword(p):
        print("Your password is good.")  
    else:
        print("Your password is not good.")

if __name__ == "__main__":
    main()
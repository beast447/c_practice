import random 
#This is a random password generator that can generate a completely random password given a length and a choice of wether or not to use special characters.

result = []
#Collect length from the user and wether or not they would like to use special characters
passwordLength = int(input("Enter the password length: "))
symbolChoice = input("Would you like to add special characters? Y for Yes and N for No: ")

#Defines the characters we can use for our generated passwords
randomChar = list("abcdefghijklmnopqrstuvwxyz")
randomDigit = list("1234567890")
randomUpper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
randomSymbol = list("!@#$%^&*")

#The funtion for getting our random password
def getRandomPassword(length, include_symbols=False):
    char_pool = randomChar + randomDigit + randomUpper

#If the user selects Y at the symbol choice input then we will include special characters in out character pool or "char_pool"
    if include_symbols:
        char_pool += randomSymbol

#Interates through the char_pool using a random integer to index our character pool list for each charater and appends that value to the results array
    for _ in range(length):
        result.append(random.choice(char_pool))

#Parses the array to a string value and returns the output
    return ''.join(result)

finalPassword = getRandomPassword(passwordLength, symbolChoice == 'Y')

print(finalPassword)
import string
import random

length = 8
#This line sets the length of the random string

str_characters = ('!@#$^&*£') + string.ascii_lowercase + string.ascii_uppercase + string.digits
#This line limits the different characters which can occur in the string
randomCode = ''.join(random.choices(str_characters, k=length))
print(randomCode + " is your new password.")
#This line generates the string
newPassword = 0
#This line creates the newPassword variable
newPassword = randomCode
#This line stores the generated string as the new password

input("Do you want to bruteforce the password? ")

# Brute force program
data_list = '!@#$^&*£%/' + string.ascii_lowercase + string.digits
charData = list(data_list)

brutePass = ""
while(brutePass != newPassword):
    brutePass = random.choices(charData,k=len(newPassword))
    print(brutePass)
    brutePass="".join(brutePass)
    print("The password is " + brutePass)
import random
import string

password_len = 8
charValues = string.ascii_letters + string.digits

password = ""
for i in range(password_len):
    password += random.choice(charValues)   # add each character to password

print("Your random password is:", password)
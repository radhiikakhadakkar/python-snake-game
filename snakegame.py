import random
otpgenerator=random.randint(000000,100000)
username=input("Please enter your username:")
print("Hello!! Have a great day", username)
print("Your otp for login is", otpgenerator)
password=input("Enter the otp for login:")
if password==str(otpgenerator):
    print("Login Success!")
else:
    password!=str(otpgenerator)
    print("Login Failed!")

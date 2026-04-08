# email = input("Enter email: ")


# if email == None:
#     print("email must not be empty") 
# elif '@' and '.' not in email:
#      print("'@', and'.' must be in email")
# elif not email.endswith(('.com','.net','org')):
#      print("email must end with '.com','.org','.net'")
# elif not (email[0].isalnum()) and (email[-1].isalnum()):
#      print("Email must not start or end with a special character")
# else:
#      print("Email is valid")

    
password = input("Enter password: ")
email = input("Enter email: ")

if password == None:
    print("Password must not be empty!")
elif len(password)<8:
    print("Password must be at least 8 characters ")
elif not(password[0].isupper()):
    print("Password must contain at least 1 uppercase")
elif not(password[1].islower()):
    print("Password must contain at least 1 lowercase")
elif password == email:
    print("Password must not be the same as email")
elif ' 'in password:
    print("Password must not have any space") 
elif  not((password[0].isalpha()) and (password[-1].isnumeric())): 
    print("Password must start and end with a letter and digit")
else:
    print("Correct password and email")
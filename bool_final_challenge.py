username = input("Enter username: ")
age = int(input("Enter age: "))
password = input("Enter password: ") 
email = input("Enter email:")
role = input("What role[admin or moderator]?:").strip().lower()
is_banned = True
verified = ('yahoo.com','outlook.com','gmail.com','live.com','hotmail.com')

print("="*40)

print(f"""
 User name is not empty and age is 18 and above ={username is not None and age >=18}
password at least 8 characters long and has no space ={len (password)>=8 and " " not in password}

user email not empty, contains '@' in email and email.ends with '.com' = {email is not None and '@' in email and email.endswith('.com') } 

username is a stringtype and is not None and longer than 5 character = {isinstance(username,str)and username is not None and len(username)>5}

User is either admin or moderator and either not banned or verified email = {role in ['admin','moderator']and not is_banned or email .endswith(verified)}  """)
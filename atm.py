users = ["Boakai","Fatu"]
passwords = ["passwordBoakai", "passwordFatu"]

# prompt user to enter username 
user = input("Enter username \n")

# get index for current user 
user_index = user.index(user)

if(user in users):
    password = input("Enter your password \n")
    if(password == passwords[user_index]):
        print("Welcome")
    else:
        print("Password not correct")
else:
    print("Sorry, username is not commrect.")
users = ["Boakai","Fatu"]
passwords = ["passwordBoakai", "passwordFatu"]
user_account_balance = [490, 200]
withdrawal_amount = 0

# prompt user to enter username 
user = input("Enter username \n")

# get index for current user 
user_index = user.index(user)


if(user in users):
    #prompt for password
    password = input("Enter your password \n")

    if(password == passwords[user_index]):
        print("Welcome \n")

        # display options 
        print("What do you want to do? Enter a number to select an option")
        print("1. Withdraw \n")
        print("2. Save Money \n")
        print("3. Complaints \n")

        selected_option = int(input())
        print(selected_option)

        if(selected_option == 1):
            withdrawal_amount = int(input("How much do you want to withdraw?\n"))
            if(withdrawal_amount > user_account_balance[user_index]):
                print("You cant withdraw this amount, your balance is low")
            else:
                print("Congratulation, you have withdraw from your account")
            print("Withdraw")
        elif(selected_option == 2):
            print("Saving")
        elif(selected_option == 3):
            print("Complaints")
        else:
            print("Invalid option, try again with a valid option")

    else:
        print("Password not correct")
else:
    print("Sorry, username is not correct.")
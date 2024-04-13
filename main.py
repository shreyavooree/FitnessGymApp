import control.memberOperations as memberOperations
import control.trainerOperations as trainerOperations
import control.adminOperations as adminOperations
import dbOperations.users as users

print("Welcome to the Voore Fitness Gym!")
print("To log in, enter 1")
print("To register, enter 2")

choice = input("Your choice: ")

if choice == str(1):
    username = input("Please enter your userId: ")
    password = input("Please enter your password: ")
    if users.validateUser(username, password) is not False:
        account = users.validateUser(username, password)
        if account == 1:
            memberOperations.Member(username)
        elif account == 2:
            trainerOperations.Trainer(username)
        else:
            adminOperations.Admin()
    else:
        print("Invalid Login! Restart program to try again...")
elif choice == str(2):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    accounttype = input("Enter account type (1 for Member, 2 for Trainer): ")
    users.addUser(first_name, last_name, email, password, phone, int(accounttype))
    id = users.getUserIdByPhone(phone)
    if accounttype == str(1):
            print("YOUR USER ID IS "+str(id)+". PLEASE KEEP THIS SAFE AND REMEMBER IT")
            memberOperations.Member(id)
    elif accounttype == str(2):
        trainerOperations.Trainer(id)
    else:
        print("error, exited")
else:
    print("INVALID INPUT! Restart program to try again...")

    
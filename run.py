import random
import string
from user import User

def display_user():
    '''
    Function that returns all the saved contacts
    '''
    return User.find_user()
def del_user(account):
    '''
    Function to delete a contact
    '''
    account.delete_user()

def main():
    while True:
        print("Welcome to password locker")
        print('-'*30)
        print('\n')
        print("Select a short codes to navigate: to create a new user use 'nn': To login to your account use: 'lg': To delete user use: 'dl' To find user use: 'fu' To exit use: 'ex'")
        short_code = input().lower()
        print('\n')

        if short_code == 'nn':
            print("create username")
            created_user_name = input()
            print("Want to create password? 'y' or 'n'")
            yes = input()
            
            if yes == "y":          
                print("create password")
                created_password = input()

            
                print("confirm password")
                confirm_password = input()
            else:
                pass_code = string.ascii_letters
                created_password = "".join(random.choice(pass_code) for i in range(10))

            while created_password != confirm_password:
                print("Password dont match")
                print("Enter your password")
                created_password = input()
                confirm_password = input()


            else:
                print(f"Congratulations {created_user_name}. Account creation was successful")
                print('\n')
                print("Proceed to login ")
                print("enter your username")
                user_name_entered = input()
                print("enter your password")
                password_entered = input()

        elif short_code == 'fu':
             if display_user():
                 print("Here is a list of all your users")
                 print('\n')
                 for user in display_user():
                     print(f"{user.user_name}")

                     print('\n')
                 else:
                     print('\n')
                     print("You dont seem to have any contacts saved yet")
                     print('\n')


        elif short_code == 'dl':
            print("want to delete account? 'y' 'n'")
            yes = input()
            if yes == 'y':
                del_user(User.user_list[1])
                print("Deleted successfully")
            else:
                print("Account not found") 






        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")
if __name__ == '__main__':
    main()         
                 

        short_code = input().lower()
         print('\n')


        if short_code == 'nn':
            print("create username")
            created_user_name = input()

            print("Want to create password? 'y' or 'n'")
            yes = input()
            # if yes:  

            print("create password")
            created_password = input()

            print("confirm password")
            confirm_password = input()

            while created_password != confirm_password:
                print("Password dont match")
                print("Enter your password")
                created_password = input()
                confirm_password = input()
            # else:
            #      pass_code = string.ascii_letters
            #      created_password = "".join(random.choice(pass_code) for i in range(10))     

            else:
                print(f"Congratulations {created_user_name}. Account creation was successful")
                print('\n')
                print("Proceed to login ")
                print("enter your username")
                user_name_entered = input()
                print("enter your password")
                password_entered = input()
            while user_name_entered != created_user_name or password_entered!=created_password:
                print("Invalid login credentials")
                print("Username")
                user_name_entered = input()
                print("Password")
                password_entered = input()
            else:
               print(f"Welcome {user_name_entered}.Login was successful")
        elif short_code == 'lg':
            print("welcome")
            print("Enter user name")
            default_user_name = input()

            print("enter password")
            default_password = input()
            print('\n')

            while default_user_name != 'testuser' or default_password !='67890':
                print("Wrong user name or password. Username 'testuser' and password '67890' ")
                print("enter username")
                default_user_name =input()
                print("enter password")
                default_password = input()

                print('\n')
            else:
                print("login Success")
                print('\n')
                print("-"*10)

                elif short_code == 'fu':
             if display_user():
                 print("Here is a list of all your users")
                 print('\n')
                 for user in display_user():
                     print(f"{user.user_name}")

                     print('\n')
                 else:
                     print('\n')
                     print("You dont seem to have any contacts saved yet")
                     print('\n')


        elif short_code == 'dl':
            print("want to delete account? 'y' 'n'")
            yes = input()
            if yes == 'y':
                del_user(User.user_list[1])
                print("Deleted successfully")
            else:
                print("Account not found") 
        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")

    if __name__ == '__main__':
        main()                 



import random
from user import User

def main():
    while True:
        print("Welcome to password locker")
        print('\n')
        print("Select a short codes to navigate: to create a new user use 'nn': To login to your account use: 'lg' To exit use: 'ex'")
        short_code = input().lower()
        print('\n')

        if short_code == 'nn':
            print("create username")
            created_user_name = input()

            print("create password")
            created_password = input()

            print("confirm password")
            confirm_password = input()

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
        #     else:
        #         print("login Success")
        #         print('\n')
        #         print("-"*10)
        # elif short_code == 'ex':
        #     break
        # else:
        #     print("Enter valid code to continue")

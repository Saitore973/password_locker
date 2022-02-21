import random
import string
from user import User
def create_user(user_name,password):
    '''
    function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user
def display_user():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_user()
def del_user(user):
    '''
    Function to delete a contact
    '''
    user.delete_user()

def save_User(user):
    user.save_user()

def main():
    while True:
        print("Welcome to password locker")
        print('-'*30)
        print('\n')
        print("Select a short codes to navigate: to create a new user account use 'nn': To login to your account use: 'lg': To delete user use: 'dl' To display user use: 'du' To exit use: 'ex'")
        short_code = input().lower()
        print('\n')

        if short_code == 'nn':
            print("create username")
            created_user_name = input()
            print("Want sytem to generate passowrd? 'y' or 'n'")
            yes = input()
            if yes == "y": 
                pass_code = string.ascii_letters
                create_password = "".join(random.choice(pass_code) for i in range(10)) 
                print("pasword Generated!!!") 
                continue       
                
            else:
                print("create password")
                create_password = input()

                print("confirm password")
                confirm_password = input()
               

            while create_password != confirm_password:
                print("Password dont match")
                print("Enter your password")
                create_password = input()
                confirm_password = input()
           

            else:
                print(f"Congratulations {created_user_name}. Account creation was successful")
                save_User(create_user(created_user_name,create_password))
                print('\n')
                print("Proceed to login ")
                print("enter your username")
                user_name_entered = input()
                print("enter your password")
                password_entered = input()
            while user_name_entered != created_user_name or password_entered!=create_password:
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

        elif short_code == 'du':
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
            print("Want to delete account? 'y' 'n'")
            yes = input()
            if yes == 'y':
                del_user()
                print("Deleted successfully")
            else:
                print("Account not found") 

            
            
            
            

        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")

if __name__ == '__main__':
    main()         
                 




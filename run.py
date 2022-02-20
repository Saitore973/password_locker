import random
from user import User

def main():
    while True:
        print("Welcome to password locker")
        print('\n')
        print("Select a short codes to navigate: to create a new user use 'nn': To login to your account use: 'lg To exit use: 'ex'")
        short_code = input().lower()
        print('\n')

        if short_code == 'nn':
            print("create username")
            created_user_name = input()

            print("create password")
            created_password = input()

            print("confirm password")
            confirm_password = input()

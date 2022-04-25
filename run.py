from user import User
from credentials import Credentials


def credentials():
    print('What action would you like to perform?')
    print("Enter add - add credentials")
    print("Enter show - show all credentials")
    print("Enter search - search a credential by the website")
    print("Enter delete - delete a credential")


def main():
    print("Welcome to your Password Locker")
    print("-" * 100)
    print('Create an account to store your credentials or Login if you already have an account')
    print('Enter create - create account')
    print('Enter login - login to your account')
    print("-" * 100)

    choice_1 = input()

    if choice_1 == 'create':
        print('Enter a username you would like to use for your password locker account:')
        new_username = input()
        print('Enter a password you would like to use for your password locker account:')
        new_password = input()
        print("-" * 100)

        new_user = User(new_username, new_password)
        new_user.add_user()

        credentials()

    elif choice_1 == 'login':
        print('Enter your password locker username:')
        login_username = input()
        print('Enter your password locker password:')
        login_password = input()
        print("-" * 100)

        login_existing_user = User.login(login_username, login_password)
        print('Successfully created an account. Now you can add credentials')

        if login_existing_user:
            print('Logged in successfully')
            credentials()

        else:
            print('User does\'t exist. Try again or create an account.')


if __name__ == '__main__':
    main()

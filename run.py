from user import User
from credentials import Credentials


def credentials():

    while True:
        print("-" * 100)
        print("-" * 100)
        print('What action would you like to perform?')
        print("Enter add - add credentials")
        print("Enter show - show all credentials")
        print("Enter search - search a credential by the website")
        print("Enter delete - delete a credential")
        print("-" * 100)
        print("-" * 100)

        choice_2 = input()

        if choice_2 == 'add':
            print('Enter the website name:')
            website = input()
            print('Enter the email used to login to the website:')
            email = input()
            print('Enter the username used to login to the website:')
            username = input()
            print('Enter the password used to login to the website:')
            password = input()

            new_credentials = Credentials(website, email, username, password)
            new_credentials.add_credential()

        elif choice_2 == 'show':
            for credential in Credentials.display_credentials():
                print(f'{credential.website}, {credential.email}, {credential.username}, {credential.password}')

        elif choice_2 == 'search':
            print('Enter the website name:')
            search = input()

            send_search = Credentials.search_credentials(search)

            print(f'Website - {send_search.website}')
            print(f'Email - {send_search.email}')
            print(f'Username - {send_search.username}')
            print(f'Password - {send_search.password}')

        elif choice_2 == 'delete':
            print('Enter name of website and it\'s credentials will be permanently deleted:')
            print('Warning, This action is irreversible!!!!')
            delete_credential = input()

            Credentials.delete_credential(delete_credential)


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

        print('Password locker account created successfully. Go ahead and login to your account')

        main()

    elif choice_1 == 'login':
        print('Enter your password locker username:')
        login_username = input()
        print('Enter your password locker password:')
        login_password = input()
        print("-" * 100)

        login_existing_user = User.login(login_username, login_password)

        if login_existing_user:
            print('Logged in successfully')
            credentials()

        else:
            print('User doesn\'t exist. Try again or create an account.')


if __name__ == '__main__':
    main()

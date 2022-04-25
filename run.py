from user import User
from credentials import Credentials

print("Welcome to your Password Locker")
print("-"*100)
print('Create an account to store your credentials or Login if you already have an account')
print('Enter create - create account')
print('Enter login - login to your account')
print("-"*100)

login_details = input()

if login_details == 'create':
    print('Enter a username you would like to use for your password locker account:')
    login_username = input()
    print('Enter a password you would like to use for your password locker account:')
    login_password = input()

    new_user = User(login_username, login_password)
    new_user.add_user()


def main():
    return None


if __name__ == '__main__':
    main()

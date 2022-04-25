class User:
    """This class is used to generate the User object. It reduces repetition"""

    users_list = []

    def __init__(self, username, password):
        """Acts like a constructor and is called everytime a new User objecte is created"""
        self.username = username
        self.password = password

    def add_user(self):
        """Adds the created user object into the user_list"""
        User.users_list.append(self)

    def delete_user(self):
        User.users_list.remove(self)

    @classmethod
    def login(cls, username, password):
        """Receives a username & password parameters and searches for a user in the user_list with the provided details.
        If a user is found, the user is allowed to move to the next step. Otherwise the app breaks"""
        for user in cls.users_list:
            if user.username == username and user.password == password:
                return True
            else:
                return False


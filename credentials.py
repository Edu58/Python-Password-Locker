class Credentials:

    credentials_list = []

    def __init__(self, website, email, username, password):
        self.website = website
        self.email = email
        self.username = username
        self.password = password

    def add_credential(self):
        Credentials.credentials_list.append(self)

    @classmethod
    def search_credentials(cls, website):
        for credential in cls.credentials_list:
            if credential.website == website:
                return credential
            else:
                return 'No such credentials. Try adding them first or check your spelling and try again.'

    def delete_credential(self):
        Credentials.credentials_list.remove(self)

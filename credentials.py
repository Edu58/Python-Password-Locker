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
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def search_credentials(cls, website):
        for credential in cls.credentials_list:
            if credential.website == website:
                return credential
            else:
                return 'No such credentials. Try adding them first or check your spelling and try again.'

    @classmethod
    def delete_credential(cls, website):
        for credential in cls.credentials_list:
            if credential.website == website:
                cls.credentials_list.remove(credential)
            else:
                return 'No credentials found'

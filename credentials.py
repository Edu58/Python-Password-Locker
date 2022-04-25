class Credentials:
    """This class is used to generate the Credentials object. It reduces repetition"""

    credentials_list = []

    def __init__(self, website, email, username, password):
        """Acts like a constructor and is called everytime a new Credential objecte is created"""
        self.website = website
        self.email = email
        self.username = username
        self.password = password

    def add_credential(self):
        """Adds the created credential object into the credential_list"""
        Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        """Returns the credential_list with all the credentials stord in it"""
        return cls.credentials_list

    @classmethod
    def search_credentials(cls, website):
        """Receives a website parameter and searches for a credential in the credential_list belonging to the website
        and returns the whole credential """
        for credential in cls.credentials_list:
            if credential.website == website:
                return credential
            else:
                return 'No such credentials. Try adding them first or check your spelling and try again.'

    @classmethod
    def delete_credential(cls, website):
        """Receives a website parameter and searches for a credential in the credential_list belonging to the website
                and deletes the whole credential"""
        for credential in cls.credentials_list:
            if credential.website == website:
                cls.credentials_list.remove(credential)
            else:
                return 'No credentials found'

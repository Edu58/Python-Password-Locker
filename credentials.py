class Credentials:

    credentials_list = []

    def __init__(self, website, email, username, password):
        self.website = website
        self.email = email
        self.username = username
        self.password = password

    def add_credential(self):
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        Credentials.credentials_list.remove(self)
